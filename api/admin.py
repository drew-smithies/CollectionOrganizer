from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Collection, Item, Attribute, Category


# Register your models here.
@admin.register(User)
class MyUserAdmin(UserAdmin):
  list_display = ('username', 'collection_count')
  list_display_links = ('username',)

@admin.register(Collection)
class CollectinAdmin(admin.ModelAdmin):
  list_display = ('name', 'user', 'description', 'item_count')
  list_display_links = ('name', 'user',)
  readonly_fields = ('item_count',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  list_display = ('name', 'collection', 'description')
  list_display_links = ('name',)

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
  list_display = ('id', 'category', 'value', 'item')
  list_display_links = ('id',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'collection')
  list_display_links = ('name',)
