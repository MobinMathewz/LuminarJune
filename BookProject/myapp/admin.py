from django.contrib import admin
from myapp.models import Author, MyBook
# Register your models here.


admin.site.register(MyBook)
admin.site.register(Author)