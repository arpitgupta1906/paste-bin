# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from .models import Paste
from django.urls import reverse_lazy
# Create your views here.

class PasteCreate(CreateView):
    model=Paste
    fields=['text','name']

class PasteDetail(DetailView):
    model=Paste
    template_name="pastebin/paste_detail.html"

class PasteList(ListView):
    model=Paste
    template_name="pastebin/paste_list.html"
    queryset=Paste.objects.all()
    context_object_name='queryset'

class PasteDelete(DeleteView):
    model=Paste
    success_url=reverse_lazy('pastebin_paste_list')

class PasteUpdate(UpdateView):
    model=Paste
    fields=['text','name']