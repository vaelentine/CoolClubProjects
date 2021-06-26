from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from GameApp.models import Party


class PartyDelete(DeleteView):
    model = Party
    fields = '__all__'
    template_name = "delete.html"
    success_url = reverse_lazy('party_list')