from django.db import models
# from django.contrib.auth.models import User
from account.models import User
# Create your models here.


class Answer(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # file_id = models.ForeignKey(Img_file, null=False, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.pk}'
