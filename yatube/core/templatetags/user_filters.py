from django import template

register = template.Library()


@register.filter
def add_class(value, css_class=None):
    if css_class:
        return value.as_widget(attrs={'class': css_class})
    return value
