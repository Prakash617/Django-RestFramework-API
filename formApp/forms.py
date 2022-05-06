from django import forms
from .models import addStd
class addStdForm(forms.ModelForm):
    class Meta:
        model=addStd
        fields=['stdId','stdName','stdEmail','stdPassword']

        labels={
            'stdId':'Id ','stdName':'Name ','stdEmail':'Email ','stdPassword':'Password '
        }

        widgets={
            'stdId':forms.NumberInput(attrs={'class':'form-control'}),
            'stdName':forms.TextInput(attrs={'class':'form-control'}),
            'stdEmail':forms.EmailInput(attrs={'class':'form-control'}),
            'stdPassword':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})
            }

    
