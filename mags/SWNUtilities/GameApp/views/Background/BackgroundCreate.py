from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from GameApp.models import Background


class BackgroundCreate(CreateView):
    model = Background
    fields = '__all__'
    template_name = "Form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Create new background"
        context['subheading'] = ""
        context['submit_button'] = 'Create'
        return context

    def form_valid(self, form):
        background = form.save()  # save form
        return redirect('background_update', pk=background.pk)
