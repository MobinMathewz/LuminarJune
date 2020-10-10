from django.shortcuts import render,redirect
from myapp.forms import AuthorForm,BookForm,BookEditForm
from myapp.models import Author,MyBook
# Create your views here.

def createAuthor(request):
    form = AuthorForm()
    context = {}
    context["form"] = form
    if request.method=="POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            authors = Author.objects.all()
            context["authors"] = authors
            return render(request,'myapp/createauthor.html',context)
    return render(request, "myapp/createauthor.html", context)

def createBook(request):
    form = BookForm
    context = {}
    context["form"] = form
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("listBook")
    return render(request,'myapp/createbook.html',context)


def listBook(request):
    qs = MyBook.objects.all()
    context ={}
    context["books"]=qs
    return render(request,"myapp/listbook.html",context)


def bookView(request,pk):
    obj = MyBook.objects.get(id=pk)
    context = {}
    context["book"] = obj
    return render(request,"myapp/bookview.html",context)

def bookEdit(request,pk):
    obj = MyBook.objects.get(id=pk)
    form = BookEditForm(instance=obj)
    context={}
    context["form"]=form
    if request.method=="POST":
        obj = MyBook.objects.get(id=pk)
        form = BookForm(instance=obj,data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("listBook")
        else:
            context={}
            context["form"]=BookEditForm(request.POST)
            return redirect("bookcreate")
    return render(request,'myapp/bookedit.html',context)


def bookDelete(request,pk):
    return render(request,"myapp/bookdelete.html")