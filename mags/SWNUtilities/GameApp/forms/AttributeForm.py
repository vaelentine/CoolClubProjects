from django.forms import ModelForm
from ..models import Attributes
from GameApp.utils import get_random_3d6_roll

class AttributeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].initial = get_random_3d6_roll()

    class Meta:
        model = Attributes
        fields = '__all__'
