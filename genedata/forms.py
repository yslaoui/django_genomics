from django import forms
from .models import *

class EcForm(forms.Form):
    ec_name = forms.CharField(label="EC Name", max_length=100)
    def clean(self):
        cleaned_data = super(EcForm, self).clean()
        ec_name = cleaned_data['ec_name']
        if not ec_name.isalpha():
            raise forms.ValidationError("EC name must be alphabetic, no space or punctuation")
        return cleaned_data

class GeneForm(forms.ModelForm):
    class Meta:
        model = Gene
        fields = ['entity', 'source', 
                  'start', 'stop', 
                  'start_codon', 'sequencing', 'ec']

    def clean(self):
        cleaned_data = super(GeneForm, self).clean()
        entity = cleaned_data['entity']
        start_codon = cleaned_data['start_codon']
        if not entity == 'Chromosome' and not entity == 'Plasmid':
            raise forms.ValidationError("Entity must be either chromosome or Plasmid")
        if not start_codon == '-' and not start_codon == 'U':
            raise forms.ValidationError("Start codon must be either + or U")
        return cleaned_data


