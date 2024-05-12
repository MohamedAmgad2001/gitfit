from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, Group)


class Foods(models.Model):
    name = models.CharField(max_length=200)
    calories = models.CharField(max_length=200, null=True)
    Protien = models.CharField(max_length=100, null=True)
    Fats = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    # def create_superuser(self, username, email, password=None):

    #     if password is None:
    #         raise TypeError('Password should not be none')

    #     user = self.create_user(username, email, password)
# user.is_superuser = True
#         user.is_staff = True
    #     return user


# AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    # auth_provider = models.CharField(
    #     max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    objects = UserManager()

    groups = models.ManyToManyField(Group, verbose_name=(
        'groups'), blank=True, related_name='authentication_users')
    user_permissions = models.ManyToManyField(
        'auth.Permission',  # or 'authentication.Permission' if you have a custom Permission model
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='authentication_users',
    )

    def str(self):
        return self.email
