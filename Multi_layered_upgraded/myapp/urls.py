from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('api/data/', views.api_data, name='api_data'),
    path('submit_vote/', views.submit_vote, name='submit_vote'),  # 👈 This one
]
