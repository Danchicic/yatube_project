from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class TechAuthor(TemplateView):
    template_name = 'about/tech.html'


class AboutAuthor(TemplateView):
    template_name = 'about/author.html'
