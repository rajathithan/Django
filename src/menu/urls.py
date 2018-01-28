from django.conf.urls import url

from .views import (
    Item_ListView,
    Item_DetailView,
    Item_CreateView,
    Item_UpdateView,
)

urlpatterns=[

    url(r'^create/$', Item_CreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$', Item_DetailView.as_view(),name='detail'),
    url(r'^$', Item_ListView.as_view(),name='list'),
]