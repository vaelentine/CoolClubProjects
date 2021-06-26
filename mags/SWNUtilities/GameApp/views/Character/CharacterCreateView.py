from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from GameApp.models import Character


class CharacterCreate(CreateView):
    model = Character
    fields = ['name']
    template_name = "Form.html"

    def form_valid(self, form):
        character = form.save()  # save form
        return redirect('character_update', pk=character.pk)