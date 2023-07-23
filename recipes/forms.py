from django.forms import ModelForm
from .models import recipe
from django import forms

class CreateRecipeForm(ModelForm):
    class Meta:
        model = recipe
        fields = "__all__"
        widgets = {'ingredient':forms.Textarea(attrs={
                    'placeholder':'Enter ingredients',
                    }),
                   'How_to_make':forms.Textarea(attrs={
                       'placeholder':'Enter the recipe'
                   
                   }),
                   'created_by':forms.HiddenInput()
                   }