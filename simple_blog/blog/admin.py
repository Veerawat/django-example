from django.contrib import admin

from .models import Blog

# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin): 
    list_display = ['title', 'content', 'created_by', 'created']
    search_fields = ['title', 'content']
