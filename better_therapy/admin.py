from django.contrib import admin
from .models import NewUser, Client, Therapist, Supervisor
from django.contrib.auth.models import Group

# #Mine: removed BaseUserAdmin, as I will use views and my own admin panel
# from .forms import UserAdminCreationForm, UserAdminChangeForm
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# #Mine: removed BaseUserAdmin, as I will use views and my own admin panel

# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'is_admin',)
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ()}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

# Register your models here.
admin.site.register(NewUser)
#  #Mine: gave up the form so removed UserAdmin
# admin.site.register(NewUser, UserAdmin)
admin.site.register(Client)
admin.site.register(Therapist)
admin.site.register(Supervisor)

admin.site.unregister(NewUser)

