from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      "placeholder": "Login"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "placeholder": "Password"})
    )

    class Meta:
        model = User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            "username",
            "email",
            "country",
            "password1",
            "password2",
        }

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Login"})
    )

    country = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Country"})
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "placeholder": "Password"}),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "placeholder": "Current password"}),
    )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "country",
            "first_name",
            "last_name"
        )

    username = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Login"})
    )

    country = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Country"})
    )

    email = forms.CharField(
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "First name"})
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Last name"})
    )
