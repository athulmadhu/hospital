from django import forms
from .models import appointment,doctorregdb,Patientdb,contact,Department




class appontmentForm(forms.ModelForm):
    class Meta:
        model=appointment
        fields="__all__"
        widget={}
        
class doctorregForm(forms.ModelForm):
    class Meta:
        model=doctorregdb
        fields=['email','password','doctorname','gender','specialisation','dob','address','contact','wdays']
        widget={}

class patientForm(forms.ModelForm):
    class Meta:
        model = Patientdb
        fields=['patientname','gender','address','dob','mobile','email','password']
        widget={
        }

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"
        widget={}

class departmentform(forms.ModelForm):
    class Meta:
        model = Department
        fields="__all__"
        widget={}