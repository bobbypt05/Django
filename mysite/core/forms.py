from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
			
			Fusername = forms.CharField(max_length=50,
			widget = forms.TextInput(attrs={
				'placeholder':'Username',
				'class': 'form-control'
			}))
	    	
			Ffirst_name = forms.CharField(max_length=30,
				widget = forms.TextInput(attrs={
					'placeholder':'First Name',
					'class': 'form-control'
			}))

			Flast_name = forms.CharField(max_length=30,
				widget = forms.TextInput(attrs={
						'placeholder':'Last Name',
						'class': 'form-control'
			}))

			Femail = forms.EmailField(max_length=30,
				widget = forms.TextInput(attrs={
						'placeholder':'Email',
						'class': 'form-control'
			}))

			Fpassword1 = forms.CharField(max_length=30,
				widget = forms.TextInput(attrs={
						'placeholder':'Password',
						'class': 'form-control',
						'type':'password'
			}))

			Fpassword2 = forms.CharField(max_length=30,
				widget = forms.TextInput(attrs={
						'placeholder':'Confirm Password',
						'class': 'form-control',
						'type':'password'
			}))
	    