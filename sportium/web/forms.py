from django import forms
from sportium.web.models import Player, Contacts


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
        # fields = ('first_name', 'last_name', 'date_of_birth', 'picture', 'clubs',)
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter player first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter player last name',
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs={
                    # if we don't do it via BootstrapFormMixin
                    'class': 'form-control',
                    'placeholder': 'Enter player date of birth',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    # if we don't do it via BootstrapFormMixin
                    'class': 'form-control',
                    'placeholder': 'Enter picture URL',

                }
            ),
            # 'clubs': forms.TextInput(
            #     # widget=forms.ChoiceField(choices=Player.clubs),
            #     attrs={
            #         # if we don't do it via BootstrapFormMixin
            #         'class': 'form-control',
            #     }
            # ),
        }


class DelPlayerForm(forms.ModelForm):
    def save(self, commit=True):
        # players = self.instance.player_set_all()
        # players.delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Player
        fields = ()


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Your name, please...',
                    'class': 'form-control',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Leave your message here...',
                    'class': 'form-control',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Where can we find you?',
                    'class': 'form-control',
                }
            ),
        }
