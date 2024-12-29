from django.db import models

# Create your models here.

# BOOK model 
class BOOK(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=100)
    published_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title