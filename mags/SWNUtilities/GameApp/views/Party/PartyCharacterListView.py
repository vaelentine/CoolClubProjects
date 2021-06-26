from django.views.generic.list import ListView
from GameApp.models import Party


class PartyCharacterList(ListView):
    model = Party
    template_name = 'party_characters_list.html'

    def get_context_data(self, **kwargs):
        party = Party.objects.get(id=1)
        party_characters = party.character_party.all()
        context = super().get_context_data(**kwargs)
        context['party_characters'] = party_characters
        context['party'] = party
        return context