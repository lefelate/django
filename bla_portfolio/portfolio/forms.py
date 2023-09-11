from django.forms import ModelForm
from django import forms
from .models import Blogs

class UploadForm(ModelForm):
    # title=forms.CharField( max_length=60)
    # description= forms.TextInput()
    # authname=forms.CharField(max_length=50)
    # img=forms.ImageField()
    
    class Meta:
        model=Blogs
        fields = ['title','description','authname','img']
        
        # widgets ={
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'authname': forms.TextInput(attrs={'class': 'form-control'})
        # }