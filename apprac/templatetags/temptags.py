from django import template

register = template.Library()

@register.simple_tag
def lower(value):
   """Converts a string into all lowercase"""
   return value.lower()