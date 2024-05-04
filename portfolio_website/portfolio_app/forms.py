from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'link']
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-field',
                'id': 'title',
                'required': True,
                'placeholder': 'Enter the title here'
            }
        )
    )
    description = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(
            attrs={
                'class': 'form-field',
                'id': 'description',
                'required': True,
                'placeholder': 'Describe the project here'
            }
        )
    )
    technologies = forms.CharField(
        max_length=200,
        required=True,
        label='Technologies',
        widget=forms.TextInput(
            attrs={
                'class': 'form-field',
                'id': 'technologies',
                'required': True,
                'placeholder': 'List technologies used'
            }
        )
    )
    link = forms.URLField(
        required=False,
        label='Project Link',
        widget=forms.URLInput(
            attrs={
                'class': 'form-field',
                'id': 'link',
                'placeholder': 'http://example.com'
            }
        )
    )

