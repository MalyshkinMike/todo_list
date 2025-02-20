from sys import meta_path

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE


# Create your models here.


class ToDoNode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=CASCADE, related_name='tdlist')
    is_done = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-datetime_update']
        indexes = [
            models.Index(fields=['-datetime_update'])
        ]