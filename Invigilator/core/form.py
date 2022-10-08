from django import forms
from .models import Invigilator
Choices=(('Computer Engineering','Department of Computer Engineering'),
            ('Mechanical Engineering','Department of Mechanical Engineering'),
            ('Civil Engineering','Department of Civil Engineering'),
            ('Electrical Engineering','Department of Electrical Engineering'),
            ('Chemical Engineering','Department of Chemical Engneering')
    )

class DateInput(forms.DateInput):
    input_type='date'

class AddInvigilatorForm(forms.ModelForm):
    
    class Meta:
        model=Invigilator
        fields=('staff_id','name','address','joined','department','position','qualification')
        widgets={
            'staff_id':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'joined':forms.DateInput(attrs={'class':'form-control'}),
            'department':forms.Select(choices=Choices,attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'qualification':forms.TextInput(attrs={'class':'form-control'})
            
        }