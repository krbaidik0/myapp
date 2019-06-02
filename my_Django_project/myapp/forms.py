from django import forms

from myapp.models import *


class StudentForm(forms.ModelForm):
	class Meta:
		model= student
		fields = '__all__'



class userlogin(forms.Form):
	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)