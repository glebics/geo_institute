from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'email', 'organization']:
            if fieldname in self.fields:
                self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs['autocomplete'] = 'username'
        self.fields['password1'].widget.attrs['autocomplete'] = 'new-password'
        self.fields['password2'].widget.attrs['autocomplete'] = 'new-password'
        self.fields['email'].widget.attrs['autocomplete'] = 'email'
        self.fields['organization'].widget.attrs['autocomplete'] = 'organization'

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'organization', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'organization', 'password')
