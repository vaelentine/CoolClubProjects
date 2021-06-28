from django.views.generic.list import ListView
from GameApp.models import Faction


class FactionList(ListView):
    model = Faction
    template_name = "faction_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = 'factions'
        return context
