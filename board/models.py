from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200, null=True)
    context = models.TextField(max_length=200, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)


