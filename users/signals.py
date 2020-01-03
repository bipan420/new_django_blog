#add certain things by deafult to the new user that gets created
# Here since we created the profile by ourself, we want to add that profile
# to every new user that gets created.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
