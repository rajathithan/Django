from django.db.models import Q
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView,CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import restaurantLocations
from .forms import restaurantFormCreation, restaurantLocationFormCreation

def restaurant_createView(request):
    form = restaurantLocationFormCreation(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        # obj = restaurantLocations.objects.create(
        #     name = form.cleaned_data.get('name'),
        #     location = form.cleaned_data.get('location'),
        #     category = form.cleaned_data.get('category')
        # )
        # return HttpResponseRedirect('/restaurants/')
    if form.errors:
        errors = form.errors
    template_name = 'restaurants/forms.html'
    context={"form":form,"errors":errors}
    return render(request,template_name,context)

def restaurant_listView(request):
    template_name='restaurants/restaurants_list.html'
    queryset = restaurantLocations.objects.all()
    context={
        "object_list" : queryset
    }
    return render(request,template_name,context)


class searchandlistRestaurants(ListView):
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

class restaurantDetailview(DetailView):
    queryset = restaurantLocations.objects.all()
    template_name = 'restaurants/restaurants_detail.html'

    #def get_context_data(self,*args, **kwargs):
    #   context = super(restaurantDetailview,self).get_context_data(*args , **kwargs)
    #   return context

    #def get_object(self, *args, **kwargs):
    #    rest_id = self.kwargs.get('rest_id')
    #    obj = get_object_or_404(restaurantLocations, pk=rest_id)
    #    return obj


class restaurantCreateView(CreateView):
    form_class = restaurantLocationFormCreation
    template_name = 'restaurants/forms.html'
    success_url = '/restaurants/'
