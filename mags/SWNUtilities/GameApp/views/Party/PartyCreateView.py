from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from GameApp.models import Party


class PartyCreate(CreateView):
    model = Party
    fields = ['name']
    template_name = "Form.html"

    def form_valid(self, form):
        Party = form.save()  # save form
        return redirect('party_update', pk=Party.pk)