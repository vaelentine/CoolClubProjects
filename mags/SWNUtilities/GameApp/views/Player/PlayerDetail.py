from django.views.generic.detail import DetailView
from GameApp.models import Player


class PlayerDetail(DetailView):
    model = Player
    template_name = "player_detail.html"
    fields = '__all__'
