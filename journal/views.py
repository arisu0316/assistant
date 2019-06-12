from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Journal
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class JournalList(LoginRequiredMixin,ListView):
    model = Journal
    ordering = ['-id']

class JournalCreate(LoginRequiredMixin,CreateView):
    model = Journal
    fields = ['content']
    success_url = '/journal/'
    template_name = 'form.html'

class JournalUpdate(LoginRequiredMixin,UpdateView):
    model = Journal
    fields = ['content']
    success_url = '/journal/'
    template_name = 'form.html'

class JournalDelete(LoginRequiredMixin,DeleteView):
    model = Journal
    success_url = '/journal/'
    template_name = 'confirm_delete.html'