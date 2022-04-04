from django import forms
from sportium.web.models import Player


class RegisterPlayerForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    # to have the user creating this pet
    def save(self, commit=True):
        # commit=False does not persist to the database, just returns the object to be created
        player = super().save(commit=False)

        player.user = self.user
        if commit:
            player.save()

    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'date_of_birth', 'picture', 'clubs',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    # if we don't do it via BootstrapFormMixin
                    # 'class': 'form-control',
                    'placeholder': 'Enter player first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    # if we don't do it via BootstrapFormMixin
                    # 'class': 'form-control',
                    'placeholder': 'Enter player last name',
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs={
                    # if we don't do it via BootstrapFormMixin
                    # 'class': 'form-control',
                    'placeholder': 'Enter player date of birth',
                }
            ),
        }
