from django.db import models

# Create your models here.
from account.models import User
from answers.models import Answer
from posts.models import Post


class Comment(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # file_id

    def __str__(self):
        return f'{self.pk}'


class PostComment(Comment):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)


class AnswerComment(Comment):
    answer = models.ForeignKey(Answer, null=True, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)

