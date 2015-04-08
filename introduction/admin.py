from django.contrib import admin
from .models import Menu, Category, Info, Picture, Contact

class MenuAdmin(admin.ModelAdmin):
    list_display = ["name_mn"]


class CatAdmin(admin.ModelAdmin):
    list_display = ["name_mn", "menuID"]


class InfoAdmin(admin.ModelAdmin):
    list_display = ["title_mn", "description_en", "published_date"]


class PicAdmin(admin.ModelAdmin):
    list_display = ["image", "alt", "infoID"]

class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "subject" , "name", "message", "sent_at"]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CatAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(Picture, PicAdmin)
# Register your models here.
