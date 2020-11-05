from django.contrib import admin
from better_therapy.models import NewUser, Client, Therapist, Supervisor

# Register your models here.
admin.site.register(NewUser)
admin.site.register(Client)
admin.site.register(Therapist)
admin.site.register(Supervisor)

