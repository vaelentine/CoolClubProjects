from GameApp.models import Attributes
from django.views.generic import CreateView
from GameApp.forms.AttributeForm import AttributeForm
from django.shortcuts import render, redirect

class AttributeCreate(CreateView):
    model = Attributes
    form_class = AttributeForm
    template_name = "Form.html"

    def form_valid(self, form):
        character = form.save()  # save form
        return redirect('character_update', pk=character.pk)
