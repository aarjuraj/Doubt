from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class QDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddQView(CreateView):
    model = Post
    template_name = 'addq.html'
    fields = '__all__'
