from django.urls import path
from .views import hello, employees

urlpatterns = [
    path('hello/', hello),
    path('employees/', employees)
]