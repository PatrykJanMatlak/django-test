from django import forms
from .models import Item
from .models import RestaurantLocation

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','restaurant','contents','excludes','public']

    def __init__(self , user=None ,*args, **kwargs):
        print(user)
        super(ItemForm,self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner = user)