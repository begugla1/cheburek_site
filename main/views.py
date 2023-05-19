from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView

from .forms import *
from .models import Contacts


def index(request):
    return render(request, 'main/index.html', {'title': 'О нас'})


def create_result(request, data):
    return render(request, 'news/create_result.html', data)


class ContactsFormAdd(CreateView):
    form_class = ContactsForm
    template_name = 'main/contacts_form.html'
    success_url = reverse_lazy('contacts')


class ContactsList(ListView):
    model = Contacts
    template_name = 'main/contacts.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contacts.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты персонала'

        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('news_home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('news_home')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('login')


class Feedback(FormView):
    form_class = FeedbackForm
    template_name = 'main/feedback.html'
    success_url = reverse_lazy('news_home')

    def form_valid(self, form):
        return redirect('news_home')

