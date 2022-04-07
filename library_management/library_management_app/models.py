from pydoc import describe
from pyexpat import model
from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    describe = models.TextField(max_length=500)


    def __str__(self):
        return self.title