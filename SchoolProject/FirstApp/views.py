from django.shortcuts import render

# Create your views here.


def getLoginPage(request):
    return render(request, 'student/login.html')