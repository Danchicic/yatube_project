from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from .forms import CreationForm, ContactForm
from django import forms


# Create your views here.
class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('post:main')
    template_name = 'users/signup.html'


class UserChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "users/password_change_form.html"

    def form_valid(self, form):
        print('отправил форму')
        send_mail('Yatube-change_password',
                  'Вы изменили пароль в своей учетной записи',
                  'popki@mail.com',
                  [self.request.user.email])
        return super().form_valid(form)


class UserContact(View):
    template_name = 'users/contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['body']
            form.save()
            return redirect('/thank-you/')

        return render(request, self.template_name, {'form': form})
