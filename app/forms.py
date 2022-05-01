from django import forms

from .models import CardOfMainSlider


class StudentForm(forms.ModelForm):
    class Meta:
        model = CardOfMainSlider
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'uk-input'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }
    file = forms.ImageField()

