from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

from restaurants.models import restaurantLocations

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(restaurantLocations)
    #item fields
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='separate each item with a comma')
    excludes = models.TextField(blank=True,null=True,help_text='separate each item with a comma')
    public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified','-created']

    def get_absolute_url(self):
        return reverse('menu:detail',kwargs={'pk':self.pk})

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")

