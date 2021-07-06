from GameApp.models import Faction
from django.views.generic import CreateView
from django.shortcuts import render, redirect


class FactionCreate(CreateView):
    model = Faction
    fields = '__all__'
    template_name = "Form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Create new background"
        context['subheading'] = ""
        context['submit_button'] = 'Create'
        return context

    def form_valid(self, form):
        faction = form.save()
        return redirect('faction_update', pk=faction.pk)