from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..forms import CharacterDetail
from ..models import Character


class CharacterList(ListView):
    model = Character
    template_name = "character_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = 'Characters'
        return context

class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"
    fields = '__all__'


class CharacterCreate(CreateView):
    model = Character
    fields = ['name']
    template_name = "Form.html"

    def form_valid(self, form):
        character = form.save()  # save form
        return redirect('character_update', pk=character.pk)

class CharacterUpdate(UpdateView):
    model = Character
    template_name = "update.html"
    fields = '__all__'

    def form_valid(self, form):
        character = form.save()  # save form
        return redirect('character_detail', pk=character.pk)

class CharacterDelete(DeleteView):
    model = Character
    fields = '__all__'
    template_name = "delete.html"
    success_url = reverse_lazy('character_list')

