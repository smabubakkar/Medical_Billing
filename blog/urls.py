from django.urls import path
from . import views
urlpatterns = [
    path('', views.stock, name='post_list'),
]