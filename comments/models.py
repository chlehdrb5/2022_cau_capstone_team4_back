from django.db import models

# Create your models here.
from account.models import User
from answers.models import Answer
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    answer = models.ForeignKey(Answer, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}'
