from django import forms
from ..models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'last_name',
            'first_name',
            'address',
            'age',
            'phone_number',
        ]