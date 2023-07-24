from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField





class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField()
    image = models.ImageField(default='postimg_def.jpg', upload_to='Posts_pics/%y/%m/%d')
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="meep_like", blank=True)
    
    
    def number_of_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.pk])
    
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-post_date',)
        
        
        
class Comment(models.Model):
    body = models.TextField(null=True)
    coment_date = models.DateTimeField(default = timezone.now)
    name = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,null=True, on_delete=models.CASCADE, related_name='comment')
    
    
    def __str__(self):
        return f'{self.name} commented on {self.post}'
    
    class Meta:
        ordering = ('-coment_date', )