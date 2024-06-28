from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Удаление help_text для каждого поля
        for fieldname in ['username', 'password1', 'password2', 'email', 'organization']:
            if fieldname in self.fields:
                self.fields[fieldname].help_text = None

    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # Указание вашей кастомной модели пользователя
        fields = UserCreationForm.Meta.fields + ('email', 'organization',)  # Добавление дополнительных полей
