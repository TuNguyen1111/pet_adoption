from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from ..models import User


class RegistrationForm(UserCreationForm):
    error_messages = {
        "password_mismatch": _("Mật khẩu không khớp"),
    }
    password1 = forms.CharField(
        label=_("Mật khẩu"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        # TODO: change to vietnamese
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Xác thực mật khẩu"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Nhập lại mật khẩu"),
    )


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'address',
            'phone_number',
        ]
        labels = {
            'username': 'Tên tài khoản',
            'first_name': 'Họ',
            'last_name': 'Tên',
            'address': 'Địa chỉ',
            'phone_number': 'Số điện thoại',
        }    

