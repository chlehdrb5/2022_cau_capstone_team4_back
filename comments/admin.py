from django.contrib import admin

# Register your models here.
from comments.models import Comment, AnswerComment, PostComment

admin.site.register(Comment)
admin.site.register(PostComment)
admin.site.register(AnswerComment)
