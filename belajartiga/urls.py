from django.urls import path, include
from .views import get_data, post_data
urlpatterns = [
    path('', get_data, name='belajartiga'),
    path('create',post_data, name="usercreate")

]