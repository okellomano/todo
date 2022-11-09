from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=150)

    def __str__(self):
        return self.title
