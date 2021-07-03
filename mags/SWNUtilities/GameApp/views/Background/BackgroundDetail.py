from django.views.generic.detail import DetailView
from GameApp.models import Background


class BackgroundDetail(DetailView):
    model = Background
    template_name = "detail_template.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'fragment_background_detail.html'
        return context
