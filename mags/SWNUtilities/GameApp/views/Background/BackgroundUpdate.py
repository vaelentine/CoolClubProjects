from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from GameApp.models import Background


class BackgroundUpdate(UpdateView):
    model = Background
    template_name = "Form.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = f"Update {self.object.name}?"
        context['subheading'] = ""
        context['submit_button'] = 'Proceed'
        return context


    def form_valid(self, form):
        background = form.save()  # save form
        return redirect('background_detail', pk=background.pk)
