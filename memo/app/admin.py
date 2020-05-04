from django.contrib import admin

from .models import Memo


class MemoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    list_display_links = ("id", "title")


admin.site.register(Memo, MemoAdmin)
