from GameApp.models import Attributes, Character
from django.views.generic import CreateView
from GameApp.forms.AttributeForm import AttributeForm
from django.shortcuts import render, redirect
from random import randint


class AttributeCreate(CreateView):
    model = Attributes
    form_class = AttributeForm
    template_name = "Form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Character Attributes"
        context['heading'] = "These are your randomly generated attributes."
        context['subheading'] = "boost one value to 14"
        context['submit_button'] = 'Save and proceeed to backgrounds'
        return context

    def form_valid(self, form):
        character = Character.objects.get(pk=self.kwargs.get('pk'))
        attribute = form.save()  # save form
        character.attributes = Attributes.objects.get(pk=attribute.pk)
        character.save()
        return redirect('add_background', pk=character.pk)
