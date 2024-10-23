from django.urls import  path
from .views import get_user,post_user

urlpatterns =[
    path('', get_user, name='userempat'),
    path('create/', post_user)
]