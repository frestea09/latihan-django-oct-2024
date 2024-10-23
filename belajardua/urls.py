from django.urls import path
from .views import get_user,post_user

urlpatterns = [
    path('users/', get_user, name="users"),
    path('users/create',post_user, name="usercreate")
]