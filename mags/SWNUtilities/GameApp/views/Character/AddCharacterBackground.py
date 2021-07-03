from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from GameApp.forms import CharacterDetail
from GameApp.models import Character


class AddCharacterBackground(UpdateView):
    model = Character
    template_name = "Form.html"
    form = CharacterDetail
    fields = [
        'background',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Choose A background"
        context['subheading'] = ""
        context['submit_button'] = 'Proceed to Skills?'
        return context

    def form_valid(self, form):
        character = form.save()  # save form
        return redirect('skills_choice', pk=character.pk)
