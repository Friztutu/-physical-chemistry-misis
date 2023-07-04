from django import forms
from Calculus.models import Task1


class Task1Form(forms.ModelForm):
    power = forms.IntegerField(min_value=1)
    scheme = forms.CharField(widget=forms.Select(choices=Task1.SCHEMES))
    climate_zone = forms.CharField(widget=forms.Select(choices=Task1.ZONES))
    soil = forms.CharField(widget=forms.Select(choices=Task1.SOILS))

    class Meta:
        model = Task1
        fields = ('power', 'scheme', 'climate_zone', 'soil')
