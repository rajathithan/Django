from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models import restaurantLocations

def restaurant_listView(request):
    template_name='restaurants/restaurants_list.html'
    queryset = restaurantLocations.objects.all()
    context={
        "object_list" : queryset
    }
    return render(request,template_name,context)

class searchandlistRestaurants(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = restaurantLocations.objects.filter(
                Q(category__iexact = slug)|
                Q(category__icontains = slug)
            )
        else:
            queryset = restaurantLocations.objects.none()
        return queryset






