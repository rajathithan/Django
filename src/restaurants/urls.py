from django.conf.urls import url


from .views import (
    #restaurant_createView,
    #restaurant_listView,
    searchandlistRestaurants,
    restaurantDetailview,
    restaurantCreateView,
)

urlpatterns = [
    #url(r'$', restaurant_listView,name='list'),
    #url(r'^restaurants/create/$', restaurant_createView),
    #url(r'^restaurants/(?P<slug>\w+)/$', searchandlistRestaurants.as_view(),name='restaurants'),
    url(r'^$', searchandlistRestaurants.as_view(),name='list'),
    url(r'^create/$', restaurantCreateView.as_view(),name='create'),
    url(r'^(?P<slug>[\w-]+)/$', restaurantDetailview.as_view(),name='detail'),

]
