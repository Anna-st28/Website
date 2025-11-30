from django.db import models
from django.contrib.auth.models import User


class PhotographerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_intro = models.CharField(max_length=250, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Photo(models.Model):
    photographer = models.ForeignKey(PhotographerProfile, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photographs')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo by {self.photographer.user.username}"
