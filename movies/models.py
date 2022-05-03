from distutils import text_file
from pyexpat import model
from unicodedata import name
from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class Movie(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    release_date = models.DateField(_("Release Date"), auto_now_add=False)
    duration = models.FloatField(_("Duration in minutes"), default=0)
    cover = models.CharField(_("Url Cover"), max_length=250)
    cover1 = models.CharField(_("Url Cover1"), max_length=250, null=True, blank=True)
    cover2 = models.CharField(_("Url Cover2"), max_length=250, null=True, blank=True)
    trailer = models.CharField(_("Url Trailer"), max_length=250)
    recap = models.TextField(_("Recap"))
    fav = models.BooleanField(_("Favorite"), default=False)
    rate = models.FloatField(_("Rate"), default=0)
    created_at = models.DateTimeField(_("Created At"), auto_now=True)
    created_by = models.ForeignKey(User, verbose_name=_("Created by"), on_delete=models.CASCADE)
    public = models.BooleanField(_("Public"), default=False)
    
    def __str__(self):
        return "%s (%s)" % (self.title, self.release_date.year)
