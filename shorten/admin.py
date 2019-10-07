from django.contrib import admin

from .models import ShortenedUrl


class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'shortened_id', 'created_at']


admin.site.register(ShortenedUrl, ShortenedUrlAdmin)
