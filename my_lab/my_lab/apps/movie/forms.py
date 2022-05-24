from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from . import models
import re

movie_name_pattern = re.compile("^[a-zA-Z0-9\s]*$")
member_name_pattern = re.compile("^[a-zA-Z\s]*$")


class MovieRentalForm(forms.ModelForm):
    return_date = forms.DateInput()

    class Meta:
        model = models.MovieRental
        fields = ['member_id', 'movie_id', 'return_date']
        widgets = {
            'member_id': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'movie_id': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'return_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

    def clean_return_date(self):
        return_date = self.cleaned_data['return_date']
        if return_date.date() < datetime.now().date():
            raise ValidationError("Invalid return date")
        return return_date


class MemberNameForm(forms.Form):
    Choices = [(data['id'], data['member_name']) for data in models.Member.objects.all().values('member_name', 'id')]
    member_name = forms.ChoiceField(choices=Choices, widget=forms.Select(attrs={'class': 'form-control'}))