from django.contrib import admin
from .models import Profile, Skill, Project, Education

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    search_fields = ['name', 'email', 'title']
    list_editable = ['title']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'order']
    list_editable = ['percentage', 'order']
    search_fields = ['name']
    ordering = ['order']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'tech1', 'tech2', 'link']
    search_fields = ['title', 'description']
    list_filter = ['tech1', 'tech2']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'duration']
    search_fields = ['degree', 'institution']
    list_filter = ['duration']