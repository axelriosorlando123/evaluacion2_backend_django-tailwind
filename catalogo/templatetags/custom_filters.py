from django import template

register = template.Library()

@register.filter
def pluck(queryset, key):
    """
    Extrae los valores de un campo de una lista de diccionarios.
    Ejemplo: [{'nombre': 'A'}, {'nombre': 'B'}] -> ['A', 'B']
    """
    return [item.get(key) for item in queryset]

