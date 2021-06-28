from django.views.generic.detail import DetailView
from GameApp.models import Faction


class FactionDetail(DetailView):
    model = Faction
    template_name = "faction_detail.html"
    fields = '__all__'
