from django.contrib import admin

from apps.file.models import File

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')

admin.site.register(File, FileAdmin)