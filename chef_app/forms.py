from django import forms
from .models import Chefs

class ChefForm(forms.ModelForm):
    class Meta:
        model = Chefs
        fields = "__all__"
