from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class NewUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('You need an email to create a user')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last seen', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = NewUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Client(NewUser):
    f_name = models.CharField(verbose_name='first name', max_length=30)
    l_name = models.CharField(verbose_name='last name', max_length=30)
    ph_num = models.CharField(verbose_name='phone number', max_length=10)


class Therapist(Client):
    is_therapist = models.BooleanField(default=True)


class Supervisor(Therapist):
    is_supervisor = models.BooleanField(default=True)




