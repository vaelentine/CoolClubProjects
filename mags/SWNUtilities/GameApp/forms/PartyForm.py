from django.forms import ModelForm
from ..models import Party


class CharacterDetail(ModelForm):
    class Meta:
        model = Party
        fields = '__all__'