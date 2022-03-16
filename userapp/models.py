import password as password
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import (EmailField, CharField, BooleanField, DateTimeField)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, first_name=None, family_name=None,
                    is_active=True, is_staff=None, is_admin=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.first_name = first_name
        user.family_name = family_name
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.is_active = is_active

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, first_name=None, family_name=None):
        user = self.create_user(email, first_name=first_name, family_name=family_name, password=password,
                                is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email, password=None, first_name=None, family_name=None):
        user = self.create_user(email, first_name=first_name, family_name=family_name, password=password,
                                is_staff=True, is_admin=False)
        return user


class PostUser(AbstractBaseUser):
    email = EmailField(verbose_name='email', unique=True, max_length=200)
    first_name = CharField(verbose_name='first name', max_length=250, blank=True, null=True)
    family_name = CharField(verbose_name='family name', max_length=250, blank=True, null=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        return self.email

    def get_full_name(self):
        if self.first_name and self.family_name:
            return f'{self.first_name} {self.family_name}'
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if not self.id and not self.is_admin:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
