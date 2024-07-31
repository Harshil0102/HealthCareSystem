from dataclasses import field
#import imp
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile,User




class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','phone_number']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['age','gender','Year_of_experience','date_of_birth','address','Specialization','image']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Year_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'Specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control', 'type': 'image'}),
        }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if User.role == '2':
    #         self.fields['age'].required = True
    #         self.fields['gender'].required = True
    #         self.fields['date_of_birth'].required = True
    #         self.fields['year_of_experience'].required = True
    #         self.fields['address'].required = True
    #         self.fields['specialization'].required = True
    #         self.fields['profile_image'].required = True


    #     else:
    #         del self.fields['specialization']
    #         del self.fields['year_of_experience']

