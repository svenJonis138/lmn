from django import forms
from .models import Note, Artist, Profile, Venue, Show

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class VenueSearchForm(forms.Form):
    search_name = forms.CharField(label='Venue Name', max_length=200)


class ArtistSearchForm(forms.Form):
    search_name = forms.CharField(label='Artist Name', max_length=200)


class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text', 'photo', 'rate')  # issue 4 upload photographs with associated notes by chris


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']


class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'hometown', 'description']


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name']


class CreateVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'address']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_username(self):

        username = self.cleaned_data['username']

        if not username:
            raise ValidationError('Please enter a username')

        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError('A user with that username already exists')

        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
            raise ValidationError('Please enter your first name')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name:
            raise ValidationError('Please enter your last name')

        return last_name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError('Please enter an email address')

        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('A user with that email address already exists')

        return email

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('twitter_username', 'bio', 'favorite_artist', 'favorite_show')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class DateInput(forms.DateInput):
    input_type = 'date'


class NewShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('show_date', 'artist', 'venue')
        widgets = {
            'show_date': DateInput()
        }
