from distutils import text_file
from pyexpat import model
from unicodedata import name
from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

class Movies(models.Model):
    title = models.CharField(_("Movie Title"), max_length=250)
    release_date = models.TimeField(_("Release Date"), auto_now_add=False)
    cover = models.CharField(_("Movie Url Cover"), max_length=250)
    cover1 = models.CharField(_("Movie Url Cover1"), max_length=250, null=True, blank=True)
    cover2 = models.CharField(_("Movie Url Cover2"), max_length=250, null=True, blank=True)
    trailer = models.CharField(_("Movie Url Trailer"), max_length=250)
    recap = models.TextField(_("Movie Recap"))
    fav = models.BooleanField(_("Favorite"), default=False)
    rete = models.FloatField(_("Movie Rate"), default=0)
    created_at = models.TimeField(_("Movie created at"), auto_now=True)
    created_by = models.ForeignKey(User, verbose_name=_("Created by"), on_delete=models.CASCADE)
    public = models.BooleanField(_("Public"), default=False)
