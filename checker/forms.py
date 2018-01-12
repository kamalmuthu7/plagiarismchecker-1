from django import forms
from .models import Data
class DataForm(forms.ModelForm):
	# post = forms.CharField(max_length=280)

	class Meta:
		model = Data
		fields = ('data',)
