from django.contrib import admin
from .models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "repo_link"]



admin.site.register(Project)