from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from GameApp.forms import CharacterDetail
from GameApp.models import Character


class CharacterDelete(DeleteView):
    model = Character
    fields = '__all__'
    template_name = "delete.html"
    success_url = reverse_lazy('character_list')

