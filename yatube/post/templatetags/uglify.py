from django import template

register = template.Library()


@register.filter
def uglify(text):
    change_text = ''
    for i in range(len(text)):
        if i % 2 == 0:
            change_text += text[i].lower()
        else:
            change_text += text[i].upper()

    return change_text
