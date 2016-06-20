from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager


class CustomerUserManager(UserManager):
    pass



class CustomerUser(AbstractUser):


    objects = CustomerUserManager()
