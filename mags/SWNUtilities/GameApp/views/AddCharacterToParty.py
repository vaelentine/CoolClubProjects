from django.shortcuts import render

from ..forms.PartyCharacterForm import PartyCharacterChoiceForm


def CharacterChoice(request):
    context = {}
    context['form'] = PartyCharacterChoiceForm
    return render(request, 'form.html', context)
