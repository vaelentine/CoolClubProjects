from django.forms import ModelForm
from ..models import Attributes


class AttributeForm(ModelForm):
    class Meta:
        model = Attributes
        fields = '__all__'

