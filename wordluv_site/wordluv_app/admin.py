from django.contrib import admin
from .models import word


class WordAdmin(admin.ModelAdmin):
    list_display = ("word", "meaning")

admin.site.register(word, WordAdmin)
