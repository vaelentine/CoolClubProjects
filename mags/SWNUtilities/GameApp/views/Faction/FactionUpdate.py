from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from GameApp.models import Faction


class FactionUpdate(UpdateView):
    model = Faction
    template_name = "Form.html"
    fields = '__all__'

    def form_valid(self, form):
        faction = form.save()  # save form
        return redirect('faction_detail', pk=faction.pk)
