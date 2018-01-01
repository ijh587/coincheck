from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    code = models.CharField(max_length=5, blank=False, null=False)
    offcURL = models.URLField(unique=True)
    offctwttr = models.URLField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['name',]

def __str__(self):
    return self.name