# coding = utf-8

from django.contrib import admin

from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):

    pass