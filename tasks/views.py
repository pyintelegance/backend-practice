from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from accounts.levels import LEVELS, get_level_by_num, get_level_index

from .checker import check
from .models import HintPurchase, Submission, Task, Topic


def catalog(request):
    topics = Topic.objects.prefetch_related('tasks').all()
    solved_tasks = set()
    user_level_index = 0
    if request.user.is_authenticated:
        user_level_index = get_level_index(request.user.profile.points)
        solved_tasks = set(
            Submission.objects.filter(
                user=request.user, status=Submission.Status.PASSED
            ).values_list('task_id', flat=True)
        )
    return render(request, 'tasks/catalog.html', {
        'topics': topics,
        'solved_tasks': solved_tasks,
        'user_level': get_level_by_num(user_level_index + 1),
        'user_level_index': user_level_index,
        'level_map': {i + 1: LEVELS[i] for i in range(len(LEVELS))},
        'total_tasks': Task.objects.count(),
        'total_topics': Topic.objects.count(),
    })


def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug)
    solved = False
    hint_purchased = False
    user_level_index = 0
    if request.user.is_authenticated:
        user_level_index = get_level_index(request.user.profile.points)
        solved = Submission.objects.filter(
            user=request.user, task=task, status=Submission.Status.PASSED
        ).exists()
        hint_purchased = HintPurchase.objects.filter(user=request.user, task=task).exists()

    required_index = task.required_level - 1
    locked = request.user.is_authenticated and (user_level_index < required_index)

    feedback = request.session.pop('last_feedback', None)
    passed = request.session.pop('last_passed', None)
    elapsed = request.session.pop('last_elapsed', None)
    last_code = request.session.pop('last_code', '')
    return render(request, 'tasks/task_detail.html', {
        'task': task,
        'solved': solved,
        'hint_purchased': hint_purchased,
        'feedback': feedback,
        'passed': passed,
        'elapsed': elapsed,
        'last_code': last_code,
        'locked': locked,
        'required_level': get_level_by_num(task.required_level),
        'user_level': get_level_by_num(user_level_index + 1),
    })


@login_required
def buy_hint(request, slug):
    task = get_object_or_404(Task, slug=slug)
    profile = request.user.profile
    if not task.hint:
        messages.error(request, 'Для этой задачи нет подсказки.')
        return redirect('task_detail', slug=task.slug)
    if HintPurchase.objects.filter(user=request.user, task=task).exists():
        messages.info(request, 'Подсказка уже куплена.')
        return redirect('task_detail', slug=task.slug)
    if profile.coins < task.hint_price:
        messages.error(request, f'Не хватает монет. Нужно {task.hint_price}.')
        return redirect('task_detail', slug=task.slug)
    profile.coins -= task.hint_price
    profile.save()
    HintPurchase.objects.create(user=request.user, task=task)
    messages.success(request, f'Подсказка куплена! (−{task.hint_price} монет)')
    return redirect('task_detail', slug=task.slug)


@login_required
def submit_solution(request, slug):
    task = get_object_or_404(Task, slug=slug)
    if request.method == 'POST':
        user_level_index = get_level_index(request.user.profile.points)
        if user_level_index < task.required_level - 1:
            messages.error(request, 'Ты ещё не достиг нужного уровня для этой задачи.')
            return redirect('task_detail', slug=task.slug)

        code = request.POST.get('code', '')
        if code.strip():
            passed, feedback, result, elapsed = check(task, code)
            status = Submission.Status.PASSED if passed else Submission.Status.FAILED
            already_solved = Submission.objects.filter(
                user=request.user, task=task, status=Submission.Status.PASSED
            ).exists()
            submission = Submission.objects.create(
                user=request.user,
                task=task,
                code=code,
                status=status,
                feedback=feedback,
            )
            if passed:
                # При успехе код очищаем (редактор будет пустым)
                request.session.pop('last_code', None)
                profile = request.user.profile
                if already_solved:
                    # Награда за задачу выдаётся только один раз
                    request.session['last_feedback'] = 'Задача решена (награда уже получена ранее).'
                else:
                    points = {Task.Difficulty.EASY: 5, Task.Difficulty.MEDIUM: 10, Task.Difficulty.HARD: 15}[task.difficulty]
                    profile.points += points
                    profile.solved_count += 1
                    profile.coins += task.reward
                    profile.save()
                    feedback_msg = f'Задача решена! +{points} очков, +{task.reward} монет'

                    # Тест уровня: решивший переходит на следующий уровень (только 1 раз)
                    if task.is_level_test:
                        cur_idx = get_level_index(profile.points)
                        if cur_idx + 1 < len(LEVELS):
                            profile.points = max(profile.points, LEVELS[cur_idx + 1]['points'])
                            profile.save()
                            level_name = get_level_by_num(get_level_index(profile.points) + 1)['name']
                            feedback_msg += f' 🎉 Ты прошёл тест уровня! Новый уровень: {level_name}'
                        else:
                            profile.save()
                    request.session['last_feedback'] = feedback_msg
            else:
                # При ошибке код сохраняем, чтобы ученик его не потерял
                request.session['last_code'] = code
                request.session['last_feedback'] = feedback
            request.session['last_passed'] = passed
            request.session['last_elapsed'] = round(elapsed, 2)
    return redirect('task_detail', slug=task.slug)


@login_required
def debug_solution(request, slug):
    """Проверка кода через AJAX без сохранения — показывает дебаг-инфо."""
    task = get_object_or_404(Task, slug=slug)
    user_level_index = get_level_index(request.user.profile.points)
    if user_level_index < task.required_level - 1:
        return JsonResponse({'error': 'Ты ещё не достиг нужного уровня для этой задачи.'})

    code = request.POST.get('code', '')
    if not code.strip():
        return JsonResponse({'error': 'Код пустой. Напиши что-нибудь.'})

    passed, feedback, result, elapsed = check(task, code)
    return JsonResponse({
        'passed': passed,
        'feedback': feedback,
        'result': result,
        'elapsed': round(elapsed, 2),
    })