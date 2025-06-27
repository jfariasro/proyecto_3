from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """Multiplica el valor por el argumento"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def div(value, arg):
    """Divide el valor por el argumento"""
    try:
        return float(value) / float(arg) if float(arg) != 0 else 0
    except (ValueError, TypeError):
        return 0

@register.filter
def dividir(value, arg):
    """Divide el valor por el argumento (alias de div)"""
    try:
        return float(value) / float(arg) if float(arg) != 0 else 0
    except (ValueError, TypeError):
        return 0

@register.filter
def promedio_puntajes(participaciones):
    """Calcula el promedio de puntajes de una lista de participaciones"""
    if not participaciones:
        return 0
    try:
        total = sum(p.puntaje for p in participaciones)
        return total / len(participaciones)
    except (AttributeError, TypeError, ZeroDivisionError):
        return 0

@register.filter
def mejor_puntaje(participaciones):
    """Obtiene el mejor puntaje de una lista de participaciones"""
    if not participaciones:
        return 0
    try:
        return max(p.puntaje for p in participaciones)
    except (AttributeError, TypeError, ValueError):
        return 0

@register.filter
def opciones_correctas(opciones):
    """Cuenta las opciones correctas"""
    try:
        return sum(1 for opcion in opciones if opcion.es_correcta)
    except (AttributeError, TypeError):
        return 0

@register.filter
def opciones_incorrectas(opciones):
    """Cuenta las opciones incorrectas"""
    try:
        return sum(1 for opcion in opciones if not opcion.es_correcta)
    except (AttributeError, TypeError):
        return 0

@register.filter
def tiene_opciones_correctas(opciones):
    """Verifica si hay al menos una opción correcta"""
    try:
        return any(opcion.es_correcta for opcion in opciones)
    except (AttributeError, TypeError):
        return False
