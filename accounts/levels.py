"""Уровни учеников. Уровень определяется по набранным очкам (points)."""

LEVELS = [
    {'name': 'Новичок', 'icon': '🌱', 'points': 0},
    {'name': 'Ученик', 'icon': '📘', 'points': 25},
    {'name': 'Кодер', 'icon': '💻', 'points': 60},
    {'name': 'Практик', 'icon': '⚙️', 'points': 120},
    {'name': 'Мастер', 'icon': '🏆', 'points': 200},
]


def get_level(points):
    """Возвращает словарь текущего уровня по очкам."""
    current = LEVELS[0]
    for level in LEVELS:
        if points >= level['points']:
            current = level
    return current


def get_level_index(points):
    """Возвращает индекс текущего уровня (0-based)."""
    index = 0
    for i, level in enumerate(LEVELS):
        if points >= level['points']:
            index = i
    return index


def get_level_by_num(num):
    """Возвращает уровень по номеру (1-based). Если номер вне диапазона — ближайший край."""
    idx = min(max(num, 1), len(LEVELS)) - 1
    return LEVELS[idx]


def get_next_level(points):
    """Возвращает следующий уровень (или None, если достигнут максимум)."""
    current_index = LEVELS.index(get_level(points))
    if current_index + 1 < len(LEVELS):
        return LEVELS[current_index + 1]
    return None


def progress(points):
    """Возвращает (текущий_уровень, следующий_уровень, прогресс_0_100)."""
    current = get_level(points)
    next_lvl = get_next_level(points)
    if next_lvl is None:
        return current, None, 100
    span = next_lvl['points'] - current['points']
    got = points - current['points']
    pct = int(got / span * 100) if span else 100
    return current, next_lvl, min(pct, 100)