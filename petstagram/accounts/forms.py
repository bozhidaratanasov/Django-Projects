from accounts.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm 

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ("profile_picture",)
