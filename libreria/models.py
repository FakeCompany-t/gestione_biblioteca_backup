from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Libro(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    data_publication = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title