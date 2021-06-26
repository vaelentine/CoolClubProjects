from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from GameApp.forms import CharacterDetail
from GameApp.models import Character


class CharacterUpdate(UpdateView):
    model = Character
    template_name = "Form.html"
    fields = '__all__'

    def form_valid(self, form):
        character = form.save()  # save form
        return redirect('character_detail', pk=character.pk)
