from django import forms


class RestaurantCreateForm(forms.Form):
    name        = forms.CharField()
    location    = forms.CharField(required = False)
    category    = forms.CharField(required = False)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Bagno":
            raise forms.ValidationError("Change it!")
        return name