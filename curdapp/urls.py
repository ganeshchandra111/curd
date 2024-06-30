from django.urls import path 
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('students/', StudentView.as_view()),
    path('students/<str:pk>/', StudentView.as_view()),
]