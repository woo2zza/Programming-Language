from django.db import models


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True)