from django.db import models

# Create your models here.

# creating table using MySql
"""create table Book(bookname varchar(10),
author varchar(20),
pages int,
category varchar(10))"""

class Book(models.Model):
    bookname = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    pages = models.IntegerField()
    price = models.IntegerField()
    category = models.CharField(max_length=120)

    def __str__(self):          #__str__ method is used when an object is to print
        return self.bookname

# orm query for creating a new object

# obj = Book(bookname="wingsoffire",author="apj",pages=250,price=250,category="autobiography")

# obj.save()

# orm query for fetching records
# book=Book.objcts.all()

# orm for fetching a corresponding record
# obj=Book.objects.get(id=1)

# obj=Book.objects.filter(pages__gte=100)