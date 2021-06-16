from django import forms
from .models import Pronouns


class PronounForm(forms.ModelForm):

    class Meta:
        model = Pronouns
        fields = (
            'gender_name',
            'subject_pronoun',
            'object_pronoun',
            'possessive_adj',
            'possessive_pronoun',
            'reflexive_pronoun'
        )


class UploadCSVForm(forms.Form):
    Upload_A_Bulk_CSV = forms.FileField()
