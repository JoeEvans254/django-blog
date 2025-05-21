from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def upload_to(instance, filename):
    return f'blog_images/{filename}'

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
