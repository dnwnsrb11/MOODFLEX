from django.urls import path
from . import views

urlpatterns = [
    path('movie_list', views.movie_list ),
]
