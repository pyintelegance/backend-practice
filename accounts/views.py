from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from tasks.models import Submission, Task

from .levels import LEVELS, get_level, get_level_index, get_next_level, progress


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна. Добро пожаловать!')
            return redirect('catalog')
        else:
            # Переводим стандартные ошибки Django на русский, чтобы ученик
            # понимал, В ЧЁМ именно проблема (логин занят / пароли не совпадают / слабый пароль).
            translate_form_errors(form)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# Словарь перевода стандартных ошибок UserCreationForm (англ. и рус. варианты)
_FORM_ERROR_TRANSLATIONS = {
    # английские (на случай, если локаль не ru)
    'A user with that username already exists.': 'Такой логин уже занят. Выбери другой.',
    'The two password fields didn’t match.': 'Пароли не совпадают.',
    'The two password fields didn\'t match.': 'Пароли не совпадают.',
    'This password is too short. It must contain at least 8 characters.':
        'Пароль слишком короткий — нужно минимум 8 символов.',
    'This password is too common.': 'Пароль слишком простой — выбери более сложный.',
    'This password is entirely numeric.': 'Пароль не может состоять только из цифр.',
    'This password is too similar to the username.':
        'Пароль слишком похож на логин — придумай другой.',
    'This field is required.': 'Это поле обязательно для заполнения.',
    # русские (текущая локаль Django)
    'Введенные пароли не совпадают.': 'Пароли не совпадают. Проверь, что оба поля одинаковые.',
    'Пользователь с таким именем уже существует.': 'Такой логин уже занят. Выбери другой.',
    'Введённый пароль слишком широко распространён.':
        'Пароль слишком простой (часто используемый). Придумай более сложный.',
    'Это поле обязательно для заполнения.': 'Это поле обязательно для заполнения.',
}


def translate_form_errors(form):
    """Заменяет английские ошибки Django на русские (in-place)."""
    for field in form:
        code = field.name
        if code in form._errors:
            form._errors[code] = [
                _FORM_ERROR_TRANSLATIONS.get(e, e) for e in form._errors[code]
            ]
    if form.non_field_errors():
        form._errors['__all__'] = [
            _FORM_ERROR_TRANSLATIONS.get(e, e) for e in form.non_field_errors()
        ]



@login_required
def profile(request):
    submissions = Submission.objects.filter(user=request.user).select_related('task')
    solved = submissions.filter(status=Submission.Status.PASSED).count()
    profile_obj = request.user.profile
    current, next_lvl, pct = progress(profile_obj.points)
    jump_price = 20 + len(LEVELS) * 5  # цена перепрыга уровня

    # Skill-тест: самая сложная задача текущего уровня (своей темы), дающая повышение
    user_lvl_num = get_level_index(profile_obj.points) + 1
    level_test = Task.objects.filter(is_level_test=True, required_level=user_lvl_num).first()
    level_test_done = False
    if level_test and request.user.is_authenticated:
        level_test_done = Submission.objects.filter(
            user=request.user, task=level_test, status=Submission.Status.PASSED
        ).exists()

    return render(request, 'accounts/profile.html', {
        'profile': profile_obj,
        'submissions': submissions[:20],
        'solved': solved,
        'level': current,
        'next_level': next_lvl,
        'level_progress': pct,
        'jump_price': jump_price,
        'level_test': level_test,
        'level_test_done': level_test_done,
        'user_lvl_num': user_lvl_num,
    })


@require_POST
@login_required
def jump_level(request):
    """Перепрыгнуть уровень за монеты."""
    profile_obj = request.user.profile
    jump_price = 20 + len(LEVELS) * 5
    if profile_obj.coins < jump_price:
        messages.error(request, f'Не хватает монет. Нужно {jump_price}.')
        return redirect('profile')
    profile_obj.points += 25  # подталкиваем к следующему уровню
    profile_obj.coins -= jump_price
    profile_obj.save()
    new_level = get_level(profile_obj.points)
    messages.success(request, f'Уровень повышен до «{new_level["name"]}»! (−{jump_price} монет)')
    return redirect('profile')


@require_POST
@login_required
def toggle_staff(request, user_id):
    target = User.objects.get(pk=user_id)
    if request.user.is_staff:
        target.is_staff = not target.is_staff
        target.save()
    return redirect('profile')


def leaderboard(request):
    users = User.objects.select_related('profile').order_by('-profile__points', '-profile__solved_count')[:20]
    ranked = []
    for u in users:
        lvl = get_level(u.profile.points)
        ranked.append((u, lvl))
    return render(request, 'accounts/leaderboard.html', {'ranked': ranked})