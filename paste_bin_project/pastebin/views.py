# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Paste
# Create your views here.

class PasteCreate(CreateView):
    model=Paste
    fields=['text','name']

class PasteDetail(DetailView):
    model=Paste
    template_name="pastebin/paste_detail.html"
