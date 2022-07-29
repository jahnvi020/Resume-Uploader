from django import forms
from .models import resume
from .widgets import DatePickerInput #Django does not give in built date picker

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
]

JOB_CITY_CHOICE=[
    ('Bangalore','Bangalore'),
    ('Chandigarh','Chandigarh'),
    ('Delhi','Delhi'),
    ('Hyderabad','Hyderabad'),
    ('Mumbai','Mumbai'),
    ('Noida','Noida'),
    ('Pune','Pune'),
    ('Anywhere','Anywhere')
]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect()) 
    # widget is applied because by default it will show as Select(List)
    jobcity=forms.MultipleChoiceField(label='Preferred Job Locations',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple())
    class Meta:
        model= resume
        fields=['id','name','email','dob','gender','locality','city','pin','state', 
        'mobile','jobtype','jobcity','profile_image','doc']  #name of fields in form
        labels={'name':'Full Name','dob':'Date of Birth','email':'Email Id','pin':'Pin Code','mobile':'Moblie Number','jobtype':'Job Role','profile_image':'Profile Image','doc':'Resume'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'dob':DatePickerInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'jobtype':forms.Select(attrs={'class':'form-control'}),
        }