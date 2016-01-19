from django import forms
from userapp.models import UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = UserProfile
		fields = ('username','password','emailid','firstname','lastname')

class UserLogin(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = UserProfile
		fields = ('username','password')
		
