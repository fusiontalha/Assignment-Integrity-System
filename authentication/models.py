from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


# CUSTOM USER MODEL 
class User(AbstractUser):
    id=models.IntegerField(primary_key=True,unique=True,auto_created=True)
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    # def __len__(self):
    #     return len(self)
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
