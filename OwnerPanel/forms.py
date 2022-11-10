
from django import forms
from listings.models import Listing
from realtors.models import Realtor


class OwnerRegistration(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"



class OwnerDetail(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = {'photo','name','phone','email','description'}