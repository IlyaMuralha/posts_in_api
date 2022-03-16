from django.contrib import admin

from notesapp.models import Note


# Не просто регистрируем модель, а переопределяем поведение админки
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
