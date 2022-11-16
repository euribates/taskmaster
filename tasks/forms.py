from django import forms

from . import models


class SearchForm(forms.Form):
    query = forms.CharField(label="buscar")
    priority = forms.MultipleChoiceField(
        label="Prioridad",
        choices=[
            ('H', "Alta"),
            ('N', "Normal"),
            ('L', "Baja"),
        ],
        widget=forms.CheckboxSelectMultiple(),
        initial=['H', 'N'],
        required=False,
    )

class ProjectAdmin(forms.ModelForm):

    def clean_end_date(self):
        
        start_date = self.cleaned_date['start_date']
        end_date = self.cleaned_date['end_date']
        if end_date <= start_date:
            raise ValidationError('La fecha de inicio debe ser anterior a la de fin')


    class Meta:
        model = models.Project
        fields = [
            'name',
            'code',
            'description',
            'start_date',
            'end_date',
        ]