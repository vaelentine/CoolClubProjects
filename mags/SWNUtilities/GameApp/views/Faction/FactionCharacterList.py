from django.views.generic.list import ListView
from GameApp.models import Faction, Character


class FactionCharacterList(ListView):
    model = Faction
    template_name = 'faction_characters_list.html'

    def get_context_data(self, **kwargs):
        faction = Faction.objects.get(pk=self.kwargs.get('pk'))
        faction_characters = Character.objects.filter(faction=faction)
        context = super().get_context_data(**kwargs)
        context['faction_characters'] = faction_characters
        context['faction'] = faction
        return context
