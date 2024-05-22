from django import forms
from .models import SecurityObject

class SecurityObjectForm(forms.ModelForm):
    class Meta:
        model = SecurityObject
        fields = ['name', 'category', 'number_of_people', 'threat_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 bg-gray-800 text-gray-200 border border-gray-700 rounded'}),
            'category': forms.Select(attrs={'class': 'w-full p-2 bg-gray-800 text-gray-200 border border-gray-700 rounded'}),
            'number_of_people': forms.Select(attrs={'class': 'w-full p-2 bg-gray-800 text-gray-200 border border-gray-700 rounded'}),
            'threat_type': forms.Select(attrs={'class': 'w-full p-2 bg-gray-800 text-gray-200 border border-gray-700 rounded'}),
        }