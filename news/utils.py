from news.models import *


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        if 'cat_selected' not in context:
            context['cat_selected'] = 'none'

        return context

