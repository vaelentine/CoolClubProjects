from django.views.generic.detail import DetailView
from GameApp.models import Party


class PartyDetail(DetailView):
    model = Party
    template_name = "party_detail.html"
    fields = '__all__'
