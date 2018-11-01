# coding = utf-8

from django.contrib import admin

from .models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    pass