from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "date_of_birth", "phone_number")


admin.site.register(models.User, UserAdmin)