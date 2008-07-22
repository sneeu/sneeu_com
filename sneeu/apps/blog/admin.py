from django.contrib import admin

from models import Post, PostComment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline', )}
    list_display = ('author', 'created', 'headline', )


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'created', 'post', )


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)