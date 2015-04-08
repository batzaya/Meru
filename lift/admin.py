from django.contrib import admin
from .models import Menu, Category, Info, Picture

class menuAdmin(admin.ModelAdmin):
    list_display = ["name_mn"]


class catAdmin(admin.ModelAdmin):
    list_display = ["name_mn", "menuID"]


class infoAdmin(admin.ModelAdmin):
    list_display = ["title_mn", "description_en", "published_date"]


class picAdmin(admin.ModelAdmin):
    list_display = ["image", "alt", "infoID"]


admin.site.register(Menu, menuAdmin)
admin.site.register(Category, catAdmin)
admin.site.register(Info, infoAdmin)
admin.site.register(Picture, picAdmin)
# Register your models here.
