from django.urls import path
from . import views

urlpatterns = [
    path('',views.getAllMovies),
    path('own/',views.getOwnMovies),
    path('add/',views.addMovie),
    path('<int:id>/update/',views.updateMovie),
    path('<int:id>/delete/',views.deleteMovie),
]