from django import forms
from .models import Pronouns
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


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

        # crispy helper requires bootstrap.. decide if you want it.
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #
        #     self.helper = FormHelper
        #     self.helper.form_method = 'post'
        #
        #     self.helper.layout = Layout(
        #         'gender_name',
        #         'subject_pronoun',
        #         'object_pronoun',
        #         'possessive_adj',
        #         'possessive_pronoun',
        #         'reflexive_pronoun'
        #     )


class UploadCSVForm(forms.Form):
    Upload_A_Bulk_CSV = forms.FileField()
