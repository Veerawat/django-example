from django.db import models
from django.contrib.auth import get_user_model

from django_extensions.db.models import TimeStampedModel
from blog.models import Blog

User = get_user_model()


class Comment(TimeStampedModel):
    comment = models.TextField()
    is_spam = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog} {self.comment} {self.created_by}"
