from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # Указание вашей кастомной модели пользователя
        fields = UserCreationForm.Meta.fields + ('email', 'organization',)  # Добавление дополнительных полей, если нужно
