
from django import forms
from .models import Feedbackplease


class spalfeedback(forms.ModelForm):
    class Meta:
        model = Feedbackplease
        fields = "__all__"



