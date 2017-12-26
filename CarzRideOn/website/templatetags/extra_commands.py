from django import template

register = template.Library()


@register.simple_tag
def get_at_index(list, index):
    return list[index]


