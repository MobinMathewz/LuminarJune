from django.shortcuts import render

# Create your views here.

def getCalc(request):
    return render(request, "calculations.html")

def solve(request):
    num1 = int(request.POST.get("num1"))
    num2 = int(request.POST.get("num2"))

    res = num1+num2
    res2=num2-num1
    print("result= ", res)
    #dtl (django template language)
    context = {}
    context["add"] = res
    context["sub"] = res2
    return render(request, "calculations.html", context)

def getFact(request):
    return render(request,"factorial.html")

def factorial(request):
    num = int(request.POST.get("num1"))
    fact =1
    for i in range(1, num+1):
        fact = fact*i
    context ={}
    context["fact"] = fact
    return render(request,"factorial.html", context)

def getPrime(request):
    return render(request,"prime.html")

def prime(request):
    num = int(request.POST.get("number"))

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")
    return render(request,"prime.html")