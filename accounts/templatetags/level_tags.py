from django import template

from accounts.levels import get_level_by_num

register = template.Library()


@register.filter
def level_name(num):
    """Возвращает 'иконка Название' по номеру уровня (1-based)."""
    lvl = get_level_by_num(int(num))
    return f'{lvl["icon"]} {lvl["name"]}'


@register.filter
def split(value, sep=','):
    """Разбивает строку по разделителю в список."""
    if not value:
        return []
    return [part.strip() for part in str(value).split(sep) if part.strip()]


@register.filter
def trim(value):
    """Убирает пробелы по краям."""
    return str(value).strip() if value else ''