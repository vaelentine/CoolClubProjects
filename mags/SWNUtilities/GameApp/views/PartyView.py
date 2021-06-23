from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..forms import PartyForm
from ..models import Party


class PartyCharactersList(ListView):
    model = Party
    template_name = 'party_characters_list.html'

    def get_context_data(self, **kwargs):
        party = Party.objects.get(id=1)
        party_characters = party.character_party.all()
        context = super().get_context_data(**kwargs)
        for character in party_characters:
            context['party_characters'] = party_characters
        return context


class PartyList(ListView):
    model = Party
    template_name = "party_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = 'parties'
        return context

class PartyDetail(DetailView):
    model = Party
    template_name = "party_detail.html"
    fields = '__all__'


class PartyCreate(CreateView):
    model = Party
    fields = ['name']
    template_name = "Form.html"

    def form_valid(self, form):
        Party = form.save()  # save form
        return redirect('party_update', pk=Party.pk)

class PartyUpdate(UpdateView):
    model = Party
    template_name = "update.html"
    fields = '__all__'

    def form_valid(self, form):
        Party = form.save()  # save form
        return redirect('party_detail', pk=Party.pk)

class PartyDelete(DeleteView):
    model = Party
    fields = '__all__'
    template_name = "delete.html"
    success_url = reverse_lazy('party_list')
