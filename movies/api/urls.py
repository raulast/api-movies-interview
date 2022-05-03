from django.urls import path
from . import views

urlpatterns = [
    path('',views.getOwnsMovies),
    path('all/',views.getOwnsMovies),
    path('add/',views.addMovie),
    path('<int:id>/update/',views.updateMovie),
    path('<int:id>/delete/',views.deleteMovie),
]