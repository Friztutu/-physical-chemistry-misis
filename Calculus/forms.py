from django import forms
from Calculus.models import Task1, ResultTask1
from Calculus.calculate_tasks.task1 import main


class Task1Form(forms.ModelForm):
    power = forms.IntegerField(min_value=1)
    scheme = forms.CharField(widget=forms.Select(choices=Task1.SCHEMES))
    climate_zone = forms.CharField(widget=forms.Select(choices=Task1.ZONES))
    soil = forms.CharField(widget=forms.Select(choices=Task1.SOILS))

    def save(self, commit=True):
        task1 = super().save(commit=True)
        diameter, vertical_length, num_accurate, scheme, distance_between, section, length, depth, total_resistance, \
            normative_resistance = main(task1.power, task1.soil, task1.climate_zone, task1.scheme)

        result1 = ResultTask1(
            task=task1,
            diameter=diameter,
            vertical_length=vertical_length,
            num_accurate=num_accurate,
            scheme=scheme,
            distance_between=distance_between,
            section=section,
            length=length,
            depth=depth,
            total_resistance=total_resistance,
            normative_resistance=normative_resistance,
        )
        result1.save()
        return task1

    class Meta:
        model = Task1
        fields = ('power', 'scheme', 'climate_zone', 'soil')
