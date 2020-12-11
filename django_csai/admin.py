from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Dictionary, User


class UserModelAdmin(admin.ModelAdmin):
    list_display = ["email", "username"]

    class Meta:
        model = True


class DictionaryModelAdmin(admin.ModelAdmin):
    list_display = ["word", "label"]

    class Meta:
        model = True


admin.site.register(Dictionary, DictionaryModelAdmin)
admin.site.register(User, UserModelAdmin)

