from django.db.models.signals import post_save # this signal gets fired after an object is aved
from django.contrib.auth.models import User # this is the sender
from django.dispatch import receiver # this is the receiver
from .models import Profile 

@receiver(post_save, sender=User) 
# When a User is created, send the signal. Signal is then received by @receiver, which is handled by the following function:
def create_profile(sender, instance, created, **kwargs):
    '''
    This is responsible for the creation of a profile each time a new user is created.
    
    It takes all the arguments that post_save signal passes to it.
    One of those argument is the instance of the user, and one of those is created.
    '''
    
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
    '''
    This is responsible for the saving of a profile each time a user is saved.
    '''
    instance.profile.save()
   
    
