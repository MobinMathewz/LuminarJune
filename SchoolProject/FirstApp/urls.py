from django.urls import path
from .views import *

urlpatterns = [
    path('login', getLoginPage, name="getLogin")
]