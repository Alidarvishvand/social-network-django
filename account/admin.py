from django.contrib import admin
from .models import Relation,Profile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from django.contrib.auth.models import User


class Profileinline(admin.StackedInline):
    model = Profile
    can_delete = False

class ExtendedUserAdmin(UserAdmin):
    inlines = [Profileinline]








admin.site.unregister(User)
admin.site.register(User,ExtendedUserAdmin)
admin.site.register(Relation)
