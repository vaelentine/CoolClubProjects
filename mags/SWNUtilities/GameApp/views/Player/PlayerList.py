from django.views.generic.list import ListView
from GameApp.models import Player


class PlayerList(ListView):
    model = Player
    template_name = "player_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = 'players'
        return context
