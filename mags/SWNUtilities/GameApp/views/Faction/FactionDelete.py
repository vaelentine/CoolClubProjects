from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from GameApp.models import Faction


class FactionDelete(DeleteView):
    model = Faction
    fields = '__all__'
    template_name = "delete.html"
    success_url = reverse_lazy('faction_list')