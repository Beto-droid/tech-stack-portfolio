from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Div, Submit
from .models import UserData
from django import forms

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Div(Field('first_name'), css_class='col-md-6'),
                Div(Field('middle_name'), css_class='col-md-6'),
                Div(Field('last_name'), css_class='col-md-6'),
            ),
            Row(
                Div(Field('job_title'), css_class='col-md-6'),
                Div(Field('age'), css_class='col-md-6'),
            ),
            Field('country'),
            Field('work_experience'),
            Field('technologies'),
            Field('social_link_connect'),
            Submit('submit', 'Save Changes', css_class='btn btn-primary')
        )
