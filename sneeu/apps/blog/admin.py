from django.contrib import admin

from models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline', )}


admin.site.register(Post, PostAdmin)
