# to create filter to remove brackets in candidate detail(preferred job locations)
from atexit import register
from django import template 
register=template.Library()

@register.filter(name='remove_special_char')
def remove_chars(value,arg): #arg= arguments in filter;value=each character present in our value
    for character in arg:
        value=value.replace(character,"")
    return value