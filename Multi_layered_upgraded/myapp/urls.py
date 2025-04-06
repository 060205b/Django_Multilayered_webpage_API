from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # or whatever your view is
]
