# coding = utf-8

from django.contrib import admin

from .models import PontoTuristico

@admin.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):

    pass