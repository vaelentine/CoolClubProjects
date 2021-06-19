"""
from django.db.models import get_app, get_models

app = get_app('my_application_name')
for model in get_models(app):"""

from django import forms
from django.apps import apps


class ModelChoiceForm(forms.Form):
    models_dict = apps.all_models['GameApp']  # returns a dict of all models
    models_list = [(str(v), k) for k, v in models_dict.items()]
    models = forms.CharField(
        label='Available Models:',
        widget=forms.Select(choices=models_list)
    )
