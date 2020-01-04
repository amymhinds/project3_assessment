from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from .forms import TaskForm
from .models import Wish
# Create your views here.

# Add the following import
from django.http import HttpResponse



# Define the home view
def home(request):
#   return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    # return render(request, 'base.html')
  wish = Wish.objects.all()
  return render(request, 'wish/index.html', { 'wish': wish })


def wish_index(request):
  wish = Wish.objects.all()
  return render(request, 'wish/index.html', { 'wish': wish })


def wish_detail(request, wish_id):
  wish = Wish.objects.get(id=wish_id)
  return render(request, 'wish/detail.html', { 'wish': wish,})

class WishCreate(CreateView):
  model = Wish
  fields = ['wish']
  success_url = '/wish/'


def wish_delete(request, wish_id):
    w= Wish.objects.get(id=wish_id)
    w.delete()
    wish = Wish.objects.all()
    return render(request, 'wish/index.html', { 'wish': wish,})
  




