from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DetailView,DeleteView


def home(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request,'about_us.html')


def contact_us(request):
    return render(request,'contact_us.html')