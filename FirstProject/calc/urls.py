from django.urls import path
from .views import getCalc, solve, getFact, factorial,getPrime, prime

urlpatterns = [
    path('getcalc', getCalc, name='getcalc'),
    path('solve', solve, name="solve"),
    path('fact', getFact, name="fact"),
    path('factorial', factorial, name="factorial"),
    path('getprime', getPrime, name="getprime"),
    path('prime', prime, name=prime),
]