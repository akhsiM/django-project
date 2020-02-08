from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):  
    # Create one-to-one relationship
    # On delete of User, delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        '''
        This method exists by default for any model. 
        However we need to add new things to automatically resize large images.
        '''
        super().save()  # Call the Parent save() method
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size) # create a thumbnail with max dimensions <= output_size
            img.save(self.image.path)  # save thumbnail over large file
            
        
        
