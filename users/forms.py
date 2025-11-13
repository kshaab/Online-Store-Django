from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class StyleFormMixin:
    fields: dict[str, forms.Field]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "Введите электронную почту"})
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Повторите пароль"}
        )

class UserRegisterForm(StyleFormMixin ,UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]