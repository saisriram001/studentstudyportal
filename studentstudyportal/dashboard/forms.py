from django import forms
from .models import *
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm

class notesform(forms.ModelForm):
    class Meta:  

        model=notes
        fields=['title','description']
class hwform(forms.ModelForm):
    class Meta:  
          
        model=hw
        fields=['subject','title','description','due']

class youtubeform(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search:")

class tdform(forms.ModelForm):
    class Meta:
      model=td
      fields=['title']

class bookform(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search:")      

class dictform(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search:")

class wikiform(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search:")    

class ConversionForm(forms.Form):
    Choices = [('mass' , 'Mass') , ('length' , 'Length')]
    select = forms.ChoiceField(choices = Choices , widget = forms.RadioSelect) 

class ConversionLengthForm(forms.Form):
    Choices = [('foot' , 'Foot') , ('yard' , 'Yard')]
    input = forms.CharField(label='' , required=False , widget=forms.TextInput(
        attrs={
            'type':'number' , 'placeholder' : 'Enter'
        }
    ))
    measure1 = forms.CharField(label = '' , widget= forms.Select(choices = Choices))
    measure2 = forms.CharField(label = '' , widget= forms.Select(choices = Choices))

class ConversionMassForm(forms.Form):
    Choices = [('pounds' , 'Pounds') , ('kilogram' , 'Kilogram')]
    input = forms.CharField(label='' , required=False , widget=forms.TextInput(
        attrs={
            'type':'number' , 'placeholder' : 'Enter'
        }
    ))
    measure1 = forms.CharField(label = '' , widget= forms.Select(choices = Choices))
    measure2 = forms.CharField(label = '' , widget= forms.Select(choices = Choices))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'password1' , 'password2']
