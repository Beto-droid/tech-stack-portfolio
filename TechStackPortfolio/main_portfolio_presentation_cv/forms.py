from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CVEntry

class CVEntryForm(forms.ModelForm):
    class Meta:
        model = CVEntry
        fields = ['job_title', 'company', 'description', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Entry'))