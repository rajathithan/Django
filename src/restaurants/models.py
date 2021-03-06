from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from .validators import category_validator
from django.core.urlresolvers import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL

class restaurantLocations(models.Model):
    owner       = models.ForeignKey(User)
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120,null=True,blank=True)
    category    = models.CharField(max_length=120,null=True,blank=True,validators=[category_validator])
    created     = models.DateTimeField(auto_now_add=True,blank=True)
    modified    = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True,blank=True)

    def get_absolute_url(self):
        # return "/restaurants/{self.slug}"
        return reverse('restaurants:detail',kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name # obj.title, instance.title

def rl_pre_save(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    print('Saving..')
    print(instance.created)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

#def rl_post_save(sender, instance, *args, **kwargs):
#    print('Saved')
#    print(instance.created)
#    instance.save()

pre_save.connect(rl_pre_save,sender=restaurantLocations)

#post_save.connect(rl_post_save,sender=restaurantLocations)