from django import forms
from datetime import date

class DatasForm(forms.Form):
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    data_fim = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('data_inicio')
        fim = cleaned_data.get('data_fim')

        if inicio and fim and (fim - inicio).days < 3:
            raise forms.ValidationError("A data final deve ser pelo menos 3 dias após a data inicial.")