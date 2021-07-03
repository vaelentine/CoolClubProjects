from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from GameApp.models import Background


class BackgroundDelete(DeleteView):
    model = Background
    fields = '__all__'
    template_name = "delete.html"
    success_url = reverse_lazy('background_list')