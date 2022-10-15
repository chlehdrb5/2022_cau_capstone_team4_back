from django.db import models

# Create your models here.
from account.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    head_image = models.ImageField(upload_to='post/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
