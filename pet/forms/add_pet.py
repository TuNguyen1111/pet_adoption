from ssl import HAS_SNI
from django import forms

from ..models import Pet, Animal


class PetForm(forms.ModelForm):
    new_animal = forms.CharField(max_length=100, label='New animal', required=False)
    
    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        self.fields['animal'].required = False

    class Meta:
        model = Pet
        fields = [
            'animal',
            'new_animal',
            'name',
            'age',
            'avatar',
            'description'
        ]

    def save(self, commit=True):
        pet = super().save(commit=False)
        if commit:
            new_animal_type = self.cleaned_data.get('new_animal')
            if new_animal_type:
                new_animal = Animal(name=new_animal_type)

                if not hasattr(pet, 'animal') or not getattr(pet, 'animal'):
                    pet.animal = new_animal
                    new_animal.save()
    
            pet.save()
        return pet

