"""
from django.db.models import get_app, get_models

app = get_app('my_application_name')
for model in get_models(app):"""

from django import forms
from django.apps import apps
from ..models import Party, Character


class PartyCharacterChoiceForm(forms.Form):
    party_obj = Party.objects.get(id=1)
    non_party_char_list = Character.objects.exclude(party=party_obj)
    tuple_list = [(str(char.name), char) for char in non_party_char_list]
    choices = forms.CharField(
        label='Characters:',
        widget=forms.Select(choices=tuple_list)
    )
