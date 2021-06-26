from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from GameApp.models import Party


class PartyUpdate(UpdateView):
    model = Party
    template_name = "update.html"
    fields = '__all__'

    def form_valid(self, form):
        Party = form.save()  # save form
        return redirect('party_detail', pk=Party.pk)