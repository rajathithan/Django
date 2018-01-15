from django import forms

class restaurantFormCreation(forms.Form):
    name        = forms.CharField()
    location    = forms.CharField(required=False)
    category    = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == "Hello":
            raise forms.ValidationError("Not a Valid Name")
        return name