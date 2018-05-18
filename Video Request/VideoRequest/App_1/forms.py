from django import forms

class videoForm(forms.Form):
	videoName = forms.CharField(max_length=30,
		widget = forms.TextInput(attrs={
		'placeholder':'Title',
	}))

	videoDescription = forms.CharField(widget = forms.Textarea(attrs={
		'placeholder':'Description'
	}))