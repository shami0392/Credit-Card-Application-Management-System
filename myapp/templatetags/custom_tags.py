from django import template
register = template.Library()


@register.filter(name="mystrip")
def mystrip(data):
    data = data[1:-1]
    return data
