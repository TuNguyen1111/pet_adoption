from django import forms

from ..models import Pet, Animal


class PetForm(forms.ModelForm):
    new_animal = forms.CharField(max_length=100, label='New animal', required=False)
    
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
            choosen_animal = pet.animal
            if not choosen_animal and new_animal_type:
                new_animal = Animal(name=new_animal_type)
                pet.animal = new_animal
                new_animal.save()
            pet.save()
        return pet

