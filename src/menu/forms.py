from django import forms
from .models import Item
from restaurants.models import restaurantLocations

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public',

        ]
    def __init__(self,user=None,*args,**kwargs):
        print(user)
        super(ItemForm,self).__init__(*args,**kwargs)
        self.fields['restaurant'].queryset = restaurantLocations.objects.filter(owner=user).exclude(item__isnull=False)
