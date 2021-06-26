from django.shortcuts import render
from GameApp.forms.PartyCharacterForm import PartyCharacterChoiceForm
from GameApp.models.Party import Party
from GameApp.models.Character import Character


def character_choice(request):
    context = dict()
    context['url'] = '/party/list'
    context['url_text'] = "Back to Party list"
    if request.method == 'POST':
        form = PartyCharacterChoiceForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data['choices']
            character = Character.objects.get(name=cleaned_data)
            party = Party.objects.get(id=1)
            character.party = party
            character.save()

    context['form'] = PartyCharacterChoiceForm
    return render(request, 'form.html', context)
