from audioop import adpcm2lin
from django import forms
from ..models import AdoptRequest


class AdoptRequestForm(forms.ModelForm):
    pet_name = forms.CharField(max_length=100, label='Tên động vật')
    animal_type = forms.CharField(max_length=100, label='Loại động vật')

    class Meta:
        model = AdoptRequest
        fields = [
            'pet_name',
            'animal_type',
            'adopter_first_name',
            'adopter_last_name',
            'adopter_age',
            'adopter_address',
            'adopt_reason',
        ]
        
        labels = {
            'adopter_first_name': 'Tên',
            'adopter_last_name': 'Họ',
            'adopter_age': 'Tuổi',
            'adopter_address': 'Địa chỉ',
            'adopt_reason': 'Lí do muốn nhận nuôi',
        }

        widgets = {
            'adopt_reason': forms.Textarea(attrs={'rows': 10}),
        }

    def save(self, commit=True):
        pass
