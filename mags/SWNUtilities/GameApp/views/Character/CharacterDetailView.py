from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from GameApp.forms import CharacterDetail
from GameApp.models import Character


class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"
    fields = '__all__'
