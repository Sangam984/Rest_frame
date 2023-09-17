from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
from django.urls import reverse



def home(request):
    return render(request,"home.html")
class ListClass(ListView):
    model = Grade
    template_name = "list.html"


class ListSubjects(DetailView):
    model = Grade
    template_name = "sub.html"


class ListTitle(DetailView):
    model = Grade_sub
    template_name = "title.html"

class DetailContent(DetailView):
    model = Content
    template_name = "detail.html"