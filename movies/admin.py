from django.contrib import admin
from .models import Movie

# Register your models here.
class AdminMovie(admin.ModelAdmin):
    pass

admin.site.register(Movie, AdminMovie)