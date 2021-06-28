from django.views.generic.list import ListView
from GameApp.models import Player


class PlayerCharacterList(ListView):
    model = Player
    template_name = 'player_characters_list.html'

    def get_context_data(self, **kwargs):
        player = Player.objects.get(id=1)
        player_characters = Player.character_player.all()
        context = super().get_context_data(**kwargs)
        context['player_characters'] = player_characters
        context['player'] = player
        return context