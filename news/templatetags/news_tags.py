from django.db.models import Count
from django import template
from django.core.cache import cache

from news.models import *


register = template.Library()


# @register.simple_tag(name='cats')
# def get_category(filter=None):
#     if not filter:
#         return Category.objects.all()
#     else:
#         return Category.objects.filter(pk=filter)


@register.inclusion_tag('news/list_categories.html', name='show_cats')
def show_categories(sort=None, cat_selected='none'):
    cats = cache.get('cats')

    if not cats:

        if not sort:
            cats = Category.objects.all().annotate(Count('articles'))
        else:
            cats = Category.objects.order_by(sort).annotate(Count('articles'))

        cache.set('cats', cats, 100)

    return {'cats': cats, 'cat_selected': cat_selected}


