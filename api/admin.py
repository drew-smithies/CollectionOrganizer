from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Collection


# Register your models here.
@admin.register(Collection)
class CollectinAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_display_links = ('name',)

admin.site.register(User, UserAdmin)
