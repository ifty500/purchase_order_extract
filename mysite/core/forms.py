from django import forms

from .models import Po

choice = (('BestSeller', 'BestSeller'),
          ('TomTailor', 'TomTailor'),
          ('TomyHill', 'TomyHill'))

class PoForm(forms.ModelForm):
    #choose =forms.CharField(widget = forms.Select(choices =choice))
    class Meta:
        model = Po
        fields = ('pdf','choose',)


# class Po_sizeForm(forms.ModelForm):
#     #choose =forms.CharField(widget = forms.Select(choices =choice))
#     class Meta:
#         model = Po_size
#         fields = ('csv',)
