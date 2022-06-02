from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re

movie_accepted_chars = re.compile("^[a-zA-Z0-9\s]*$")
member_accepted_chars = re.compile("^[a-zA-Z\s]*$")


class DateInput(forms.DateInput):
    input_type = 'date'


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


class MovieForm(forms.ModelForm):
    CHOICES = [
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Detective", "Detective"),
        ("Comedy", "Comedy"),
        ("Western", "Western")
    ]
    date_of_release = forms.DateInput(attrs={'class': 'form-control'})
    genre = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea, max_length=300)
    actors = forms.ModelMultipleChoiceField(queryset=models.Actor.objects.all())
    url = forms.SlugField(max_length=150)
    imageURL = forms.ImageField()

    class Meta:
        model = models.Movie
        fields = ['title', 'date_of_release', 'genre', 'price', 'description', 'imageURL', 'actors', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields['imageURL'].required = False

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Wrong Price")
        return price

    def clean_date(self):
        year = self.cleaned_data["date_of_release"]
        if year > datetime.now().date().year:
            raise ValidationError("Wrong year")
        return year

    def clean_title(self):
        name = self.cleaned_data["title"]
        if not movie_accepted_chars.fullmatch(name):
            raise ValidationError("Please enter a correct title")
        return name.strip().title()       #убирает символы с неправильно введенной строки

    def clean_description(self):
        description = self.cleaned_data["description"]
        if not movie_accepted_chars.fullmatch(description):
            raise ValidationError("Please enter a correct description!")
        return description.strip().title()


class MemberNameForm(forms.Form):
    Choices = [(data['id'], data['member_name']) for data in models.Member.objects.all().values('member_name', 'id')]
    member_name = forms.ChoiceField(choices=Choices, widget=forms.Select(attrs={'class': 'form-control'}))


class MemberForm(forms.ModelForm):
    member_name = forms.CharField(max_length=100)
    email_address = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateInput()
    Choices = [(1, 'Male'), (2, 'Female')]
    gender = forms.ChoiceField(choices=Choices, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = models.Member
        fields = ['member_name', 'email_address', 'age', 'birthday', 'gender']
        widgets = {
            'member_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control'}),
        }

    def clean_member_name(self):
        name = self.cleaned_data["member_name"]
        if not member_accepted_chars.fullmatch(name):
            raise ValidationError("Please enter a correct name")
        return name.strip().title()

    def clean_birthday(self):
        birthday = self.cleaned_data["birthday"]
        if birthday.date() > datetime.now().date():
            raise ValidationError("Wrong date")
        return birthday

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 0:
            raise ValidationError("Wrong Age")
        return age


class ActorForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    imageURL = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea, max_length=300)

    class Meta:
        model = models.Actor
        fields = ['name', 'age', 'imageURL', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ActorForm, self).__init__(*args, **kwargs)
        self.fields['imageURL'].required = False

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 0:
            raise ValidationError("Wrong Age")
        return age

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not member_accepted_chars.fullmatch(name):
            raise ValidationError("Please enter a correct actor name")
        return name.strip().title()


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
