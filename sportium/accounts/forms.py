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
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'gender')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
        }


# class EditProfileForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.initial['gender'] = Profile.PREFER_NOT_TO_SAY
#
#     class Meta:
#         model = Profile
#         fields = '__all__'


class DelProfileForm(forms.ModelForm):
    def save(self, commit=True):
        # players = self.instance.player_set_all()
        # players.delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()
