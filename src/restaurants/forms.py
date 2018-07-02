from django import forms
from .models import RestaurantLocation
from .validators import validate_category


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category'

        ]
    # def clean_name(self):
    #     name = self.cleaned_data("name")
    #     if name == "xxx":
    #         raise forms.ValidationError("Not a valid name!")
    #     return name