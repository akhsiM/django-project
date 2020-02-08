from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # Unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    # (For the above we can also do DateTimeField(auto_now_add = True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # This specifies a many-to-one relationship
    # Also, on delete of user, also delete the post(s) as well
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
     