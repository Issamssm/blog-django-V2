from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

class Profile(models.Model):
    image = models.ImageField(default='defaultimg.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.user} profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
            
            
    
def create_profile(sender, **kwarg):
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])
        
post_save.connect(create_profile, sender=User)