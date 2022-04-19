from django.urls import path
from .views import *
urlpatterns=[
    path("new",newpart,name='NewPart'),
    path("another", anotherpart, name='AnotherPart')
]