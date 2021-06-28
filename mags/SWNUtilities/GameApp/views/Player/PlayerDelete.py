from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from GameApp.models import Player


class PlayerDelete(DeleteView):
    model = Player
    fields = '__all__'
    template_name = "delete.html"
    success_url = reverse_lazy('player_list')