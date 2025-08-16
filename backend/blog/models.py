from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(default=date.today)
    def __str__(self):
        return self.title
