from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView,CreateView, UpdateView
from .forms import ItemForm

# Create your views here.

class Item_ListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class Item_DetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class Item_CreateView(CreateView):
    template_name = 'forms.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(Item_CreateView,self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Item'
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(Item_CreateView,self).form_valid(form)


class Item_UpdateView(UpdateView):
    template_name = 'forms.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(Item_UpdateView,self).get_context_data(*args,**kwargs)
        context['title'] = 'Update Item'
        return context
