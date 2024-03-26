from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
