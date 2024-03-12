from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.core.mail import send_mail
from .forms import BookForm, CDForm
from .models import Book


# Create your views here.
class LibraryMainView(View):
    template_name = 'library/library_view.html'

    def get(self, request):
        last_ten_books = Book.objects.all()[:10]
        context = {
            'books': last_ten_books
        }
        return render(request, self.template_name, context)


class NewBookView(CreateView):
    form_class = BookForm
    template_name = 'library/new_book.html'
    success_url = '/thankyou/'


class LibraryBookView(View):
    def get(self, request):
        pass


class UserCd(View):
    form_class = CDForm
    template_name = 'library/index.html'
    success_url = '/thankyou/'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = CDForm(request.POST)

        if not form.is_valid():
            return
        send_mail('Форма from CD Site',
                  f'Вот ваш данные {form}',
                  'oursite@mail.com',
                  form.cleaned_data['email'],
                  )
