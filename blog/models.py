from django.db import models
from django.contrib.auth.models import User



class BlockUser(models.Model):
    username = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.username


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

