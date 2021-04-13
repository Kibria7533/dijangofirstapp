from django import forms
from .models import st


# creating a form
class StForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = st

        # specify fields to be used
        fields = [
            "name",
            "father_name"
        ]