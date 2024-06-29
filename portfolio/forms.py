from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            "image",
            "caption",
        ]
        widgets = {
            "image": forms.FileInput,
            "caption": forms.TextInput(attrs={"placeholder": "Enter caption"}),
        }
