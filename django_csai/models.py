from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(blank=True, null=True, max_length=120)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')


class Dictionary(models.Model):
    word = models.CharField(blank=True, null=True, max_length=200)
    label = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.word

