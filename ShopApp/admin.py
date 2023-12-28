from django.contrib import admin
from .models import type_every, item_catalog, types_item
# Register your models here.


@admin.register(type_every)
class type_everyAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(item_catalog)
class item_catalogAdmin(admin.ModelAdmin):
    list_display = ("title", "desc", "types_item", "path_image")


@admin.register(types_item)
class types_itemAdmin(admin.ModelAdmin):
    list_display = ("name",)