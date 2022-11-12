from django.db import models
# from django.contrib.auth.models import User
from account.models import User
# Create your models here.
from posts.models import Post


class Answer(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    head_image = models.ImageField(null=True, blank=True, upload_to='answer/images/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_answers')
    selected = models.BooleanField(default=False)
    # file_id = models.ForeignKey(Img_file, null=False, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.pk}'
