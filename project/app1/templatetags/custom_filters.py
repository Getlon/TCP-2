from django import template

register = template.Library()


@register.filter(name='correct_url')
def censor(url):
    url = str(url).replace('app1/static/', '')
    return url


@register.filter(name='len_restrict')
def len_restrict(str1):
    return str1[:30]
