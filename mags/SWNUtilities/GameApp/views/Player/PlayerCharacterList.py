from django.views.generic.list import ListView
from GameApp.models import Player, Character


class PlayerCharacterList(ListView):
    model = Player
    template_name = 'player_characters_list.html'

    def get_context_data(self, **kwargs):
        player = Player.objects.get(pk=self.kwargs.get('pk'))
        player_characters = Character.objects.filter(player=player)
        context = super().get_context_data(**kwargs)
        context['player_characters'] = player_characters
        context['player'] = player
        return context