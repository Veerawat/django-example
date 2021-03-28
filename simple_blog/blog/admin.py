from django.contrib import admin

from comments.models import Comment

from .models import Blog

# admin.site.register(Blog)


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ["is_spam", "comment", "created_by"]
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_by", "created"]
    search_fields = ["title", "content"]

    inlines = [CommentInline]
