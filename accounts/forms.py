from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.contrib.auth.hashers import check_password


class CustomUserCreationForm(SignupForm):
    email = forms.EmailField(
        required=True,
    )
    nickname = forms.CharField(max_length=10)
    profile = forms.ImageField(required=False)

    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        user.nickname = self.cleaned_data["nickname"]
        user.profile = self.cleaned_data["profile"]
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "nickname",
            "profile",
        )
        labels = {
            "username": "아이디",
            "email": "이메일",
            "nickname": "닉네임",
            "profile": "프로필 이미지",
        }

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(get_user_model().objects.filter(username=username)):
            raise ValidationError("중복된 아이디가 있습니다.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(get_user_model().objects.filter(email=email)):
            raise ValidationError("중복된 이메일이 있습니다.")
        return email


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "profile",
            "nickname",
        )
        labels = {
            "profile": "프로필 이미지",
            "nickname": "닉네임",
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(get_user_model().objects.filter(email=email)):
            raise ValidationError("중복된 이메일이 있습니다.")
        return


class CheckPasswordForm(forms.Form):
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error("password", "비밀번호가 일치하지 않습니다.")
