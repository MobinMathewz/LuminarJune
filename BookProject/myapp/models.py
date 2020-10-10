from django.db import models

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.author_name


class MyBook(models.Model):
    book_name = models.CharField(max_length=250, unique=True)
    pages = models.IntegerField()
    price = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    book_image = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.book_name