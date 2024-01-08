from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
class Post(models.Model):
    """the model for the blog"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        """publish function"""
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    """profile model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='taaa.jpg')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username