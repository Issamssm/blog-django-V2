from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile
from django.contrib import messages

    
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'bordder-[#E9EDF4] w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-body-color text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none mb-6', 'placeholder':'username'}),label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'bordder-[#E9EDF4] w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-body-color text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none mb-6', 'placeholder':'email'}),label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'bordder-[#E9EDF4] w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-body-color text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none mb-6', 'placeholder':'password'}), min_length=8,label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'bordder-[#E9EDF4] w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-body-color text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none mb-6', 'placeholder':'password Confirmation'}), min_length=8,label='')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_password2(self) :
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']
    
    def clean_username(self) :
        cd = self.cleaned_data
        if User.objects.filter(username = cd['username']).exists():
            raise  forms.ValidationError('Username already exists, please choose another one.')
        return cd['username']
    
    
    
class ProfileUpdate(forms.ModelForm):
    image = forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={'style' : "grid-column: span 2 / span 2; width:138px;",'class':"custom-file-input bg-[#FCFDFE]"}))

    class Meta:
        model=Profile
        fields = ('image',)
        
        
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class' : 'bordder-[#E9EDF4] w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-base text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none', 'placeholder':'username'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class' : 'bordder-[#E9EDF4] w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-base text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none', 'placeholder':'first_name'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class' : 'bordder-[#E9EDF4] w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-base text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none', 'placeholder':'last_name'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class' : 'bordder-[#E9EDF4] w-full rounded-md border bg-[#FCFDFE] py-3 px-5 text-base text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none', 'placeholder':'Email'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        
        
        
        
        
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        
