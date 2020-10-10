from django.shortcuts import render
from Book.forms import BookForm
from Book.models import Book
# Create your views here.


def bookCreate(request):
    form = BookForm()
    context = {}
    context["form"] = form
    template_name = "Book/book_create.html"
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            bookname = form.cleaned_data["bookname"]
            author = form.cleaned_data["author"]
            pages = form.cleaned_data["pages"]
            price = form.cleaned_data["price"]
            category = form.cleaned_data["category"]

            obj=Book(bookname=bookname,author=author,pages=pages,price=price,category=category)
            obj.save()

            print(bookname,",",author)
            books = Book.objects.all()
            context={}
            context["book"] = books
            template_name = "Book/book_list.html"
            return render(request,template_name,context)
        else:
            context = {}
            context["form"] = form
            return render(request, template_name, context)

    return render(request, template_name, context)