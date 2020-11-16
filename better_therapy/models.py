from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


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

    class Meta:
        permissions = (
            ('can_view_client', 'View Client'),
            ('can_update_client', 'Update Client'),
            ('can_view_client_detail', 'Client Detail'),
            ('can_view_appointment', 'Client Appointment'),  # not yet implemented badabeem
                       )

class Therapist(Client):
    is_therapist = models.BooleanField(default=True)
    supervisor_id = models.ForeignKey(null=True, to='Supervisor', on_delete=models.SET_NULL, related_name='Supervisor')

    class Meta:
        permissions = (
            ('can_view_client', 'View Client'),
            ('can_update_client', 'Update Client'),
            ('can_view_client_detail', 'Client Detail'),
            ('can_add_client', 'Add a client'),
            ('can_archive_client', 'Archive Client'),  # not yet implemented badabeem
            ('can_view_client_list', 'View Client List'),
            ('can_view_therapist_detail', 'View Therapist Detail'),  # not yet implemented badabeem
            ('can_update_therapist', 'Update Terapist'),# not yet implemented badabeem
                        )


class Supervisor(Therapist):
    is_supervisor = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('can_view_client', 'View Client'),
            ('can_update_client', 'Update Client'),
            ('can_view_client_detail', 'Client Detail'),
            ('can_add_client', 'Add a client'),
            ('can_archive_client', 'Archive Client'),   # not yet implemented badabeem
            ('can_view_client_list', 'View Client List'),
            ('can_add_therapist', 'Add Therapist'),  # not yet implemented badabeem
            ('can_view_therapist_detail', 'View Therapist Detail'),  # not yet implemented badabeem
            ('can_update_therapist', 'Update Terapist'),  # not yet implemented badabeem
            ('can_archive_therapist', 'Archive Therapist'),  # not yet implemented badabeem
                        )



class Appointment(models.Model):
    therapist = models.ForeignKey(to=Therapist, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='Client')
    date_and_time = models.DateTimeField(verbose_name='Date and time',
                                         default=timezone.now)





