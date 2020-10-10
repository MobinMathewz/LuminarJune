from django.shortcuts import render

# Create your views here.

def getReg(request):
    return render(request,"firstapp/login.html")

def formVal(request):
    email = request.POST.get("email")
    pwd = request.POST.get("pwd")

    print(email)
    print(pwd)
    context={}
    context["user"]= {"email":email, "pwd":pwd}
    return render(request,"firstapp/home.html", context)
