from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from GameApp.models import Player


class PlayerUpdate(UpdateView):
    model = Player
    template_name = "Form.html"
    fields = '__all__'

    def form_valid(self, form):
        player = form.save()  # save form
        return redirect('player_detail', pk=player.pk)
