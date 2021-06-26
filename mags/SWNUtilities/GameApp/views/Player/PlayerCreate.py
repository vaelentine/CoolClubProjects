from GameApp.models import Player
from django.views.generic import CreateView
from django.shortcuts import render, redirect


class PlayerCreate(CreateView):
    model = Player
    fields = ['name']
    template_name = "Form.html"

    def form_valid(self, form):
        player = form.save()
        return redirect('player_list')