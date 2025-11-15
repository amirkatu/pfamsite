from django.contrib import admin
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditorUploadingWidget(config_name='default'),
        }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'author', 'created_at', 'get_summary']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content', 'summary']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    
    def get_summary(self, obj):
        return obj.summary[:50] + "..." if len(obj.summary) > 50 else obj.summary
    get_summary.short_description = 'خلاصه'