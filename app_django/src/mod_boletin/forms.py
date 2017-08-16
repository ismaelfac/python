from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
   class Meta:
   	  model = Registrado
   	  fields = ["nombre","email"]

   def clean_email(self):
   	 print (self.cleaned_data)
   	 return "ismaelfac@gmail.com"

class RegForm(forms.Form):
   nombre = forms.CharField(max_length=100)
   email = forms.EmailField()