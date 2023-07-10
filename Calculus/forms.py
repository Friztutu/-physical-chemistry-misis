from django import forms
from Calculus.models import Task1, ResultTask1, Task2, ResultTask2
from Calculus.calculate_tasks.task1 import main
from Calculus.calculate_tasks.task2 import init_varibles


class Task1Form(forms.ModelForm):
    power = forms.IntegerField(min_value=100)
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


class Task2Form(forms.ModelForm):
    scheme = forms.CharField(widget=forms.Select(choices=Task2.SCHEMES))
    length = forms.IntegerField(min_value=1)
    power = forms.IntegerField(widget=forms.Select(choices=Task2.POWERS))
    phase_voltage = forms.IntegerField(min_value=1)
    phase_square = forms.IntegerField(min_value=1)
    phase_material = forms.CharField(widget=forms.Select(choices=Task2.MATERIALS))
    distance_between_conductors = forms.FloatField(min_value=0.0)
    amperage_nominal = forms.IntegerField(min_value=1)
    type_electro = forms.CharField(widget=forms.Select(choices=Task2.TYPES))

    def save(self, commit=True):
        task2 = super().save(commit=True)
        square = init_varibles(
            scheme_id=task2.scheme,
            power_key=task2.power,
            phase_voltage_db=task2.phase_voltage,
            length_db=task2.length,
            phase_square_db=task2.phase_square,
            phase_material_id=task2.phase_material,
            distance_between_conductors_db=task2.distance_between_conductors,
            amperage_nominal_db=task2.amperage_nominal,
        )

        result2 = ResultTask2(task=task2, square=square)
        result2.save()
        return task2

    class Meta:
        model = Task2
        fields = ('scheme', 'length', 'power', 'phase_voltage', 'phase_square', 'phase_material',
                  'distance_between_conductors', 'amperage_nominal', 'type_electro')
