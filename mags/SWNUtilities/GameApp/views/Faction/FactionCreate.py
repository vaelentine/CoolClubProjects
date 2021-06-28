from GameApp.models import Faction
from django.views.generic import CreateView
from django.shortcuts import render, redirect


class FactionCreate(CreateView):
    model = Faction
    fields = ['name']
    template_name = "Form.html"

    def form_valid(self, form):
        faction = form.save()
        return redirect('faction_update', pk=faction.pk)