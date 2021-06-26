from django.views.generic.list import ListView
from GameApp.models import Party


class PartyList(ListView):
    model = Party
    template_name = "party_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = 'parties'
        return context