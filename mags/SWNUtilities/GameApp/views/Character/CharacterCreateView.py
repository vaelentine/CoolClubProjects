from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from GameApp.models import Character


class CharacterCreate(CreateView):
    model = Character
    fields = []
    template_name = "Form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Create new character"
        context['subheading'] = "Proceed and roll attributes?"
        context['submit_button'] = 'Proceed'
        return context

    def form_valid(self, form):
        character = form.save()  # save form
        return redirect('attribute_creation', pk=character.pk)
