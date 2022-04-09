from django import forms
from django.contrib.auth import forms as auth_forms

from sportium.accounts.models import Profile
from sportium.common.helpers import UserModel


class CreateProfileForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )

    date_of_birth = forms.DateField()

    personal_information = forms.CharField(
        widget=forms.Textarea,
    )

    picture = forms.URLField()

    email = forms.EmailField()

    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            personal_information=self.cleaned_data['personal_information'],
            picture=self.cleaned_data['picture'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'gender', 'date_of_birth',
                  'personal_information', 'picture')

        # widgets = {
        #     'username': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Enter username',
        #         }
        #     ),
        #     'password1': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Enter your password',
        #         }
        #     ),
        #     'password2': forms.PasswordInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Confirm your password',
        #         }
        #     ),
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Enter first name',
        #         }
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Enter last name',
        #         }
        #     ),
        #     'gender': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #         }
        #     ),
        #     'date_of_birth': forms.DateInput(
        #         attrs={
        #             'class': 'form-control',
        #         }
        #     ),
        #     'personal_information': forms.Textarea(
        #         attrs={
        #             'class': 'form-control',
        #             'rows': 3,
        #         }
        #     ),
        #     'picture': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Enter picture URL',
        #         }
        #     ),
        #
        # }


class DelProfileForm(forms.ModelForm):
    def save(self, commit=True):
        # players = self.instance.player_set_all()
        # players.delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()
