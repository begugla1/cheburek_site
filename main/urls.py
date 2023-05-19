from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.ContactsList.as_view(), name='contacts'),
    path('contacts_form', views.ContactsFormAdd.as_view(), name='contacts_form'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.LogoutUser.as_view(), name='logout'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('feedback', views.Feedback.as_view(), name='feedback')
]