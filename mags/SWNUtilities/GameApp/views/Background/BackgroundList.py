from django.views.generic.list import ListView
from GameApp.models import Background


class BackgroundList(ListView):
    model = Background
    template_name = "list_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = 'background'
        return context
