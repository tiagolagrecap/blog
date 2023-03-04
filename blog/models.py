from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django_limits.limiter import Limiter


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



