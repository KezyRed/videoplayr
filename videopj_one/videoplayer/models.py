from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('video_detail', args=[str(self.id)])

class Presentation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    presentation_file = models.FileField(upload_to='presentations/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    
    # Используем settings.AUTH_USER_MODEL для гибкости
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,  # Если пользователь удален, автор остается
        null=True,  # Разрешаем null
        blank=True  # Разрешаем пустое поле в формах
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('presentation_detail', args=[str(self.id)])