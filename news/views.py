from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ArticlesForm
from .utils import DataMixin
from .models import *


class NewsHome(DataMixin, ListView):
    model = Articles
    template_name = 'news/news_home.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Articles.objects.filter(is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Новости')
        return context | c_def


class NewsHomeCat(DataMixin, ListView):
    model = Articles
    template_name = 'news/news_home.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return Articles.objects.filter(is_published=True, cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(cat_selected=c.slug,
                                      title=f"Категория: {str(c.name)}")
        return context | c_def


class HomeDetail(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'
    slug_url_kwarg = 'art_slug'


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete_view.html'
    success_url = reverse_lazy('news_home')
    slug_url_kwarg = 'art_slug'


class NewsUpdateView(UpdateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'news/update_view.html'
    slug_url_kwarg = 'art_slug'


class HomeCreate(LoginRequiredMixin, CreateView):
    form_class = ArticlesForm
    template_name = 'news/create.html'
    success_url = reverse_lazy('success_creation')
    login_url = reverse_lazy('register')
    raise_exception = False


def create_result(request):
    return render(request, 'news/create_result.html')

