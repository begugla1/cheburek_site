from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.NewsHome.as_view(), name='news_home'),
    path('create', views.HomeCreate.as_view(), name='create'),
    path('create/success', views.create_result, name='success_creation'),
    path('<slug:cat_slug>', views.NewsHomeCat.as_view(), name='news_category'),
    path('<slug:cat_slug>/<slug:art_slug>', views.HomeDetail.as_view(), name='news_detail'),
    path('<slug:cat_slug>/<slug:art_slug>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<slug:cat_slug>/<slug:art_slug>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
]

