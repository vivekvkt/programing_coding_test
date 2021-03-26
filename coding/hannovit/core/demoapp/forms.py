from django import forms
from .models import Patient
from django.forms import ModelForm

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__' # ['firstname','lastname','gender','dob'] #'__all__'



class EditPatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['firstname','dob'] #'__all__'



    
