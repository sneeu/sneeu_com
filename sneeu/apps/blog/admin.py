from django.contrib import admin
from django.forms.models import modelform_factory

from forms import PostAdminForm
from models import Post, PostComment


class LimitForeignKeyAdmin(admin.ModelAdmin):
    pass


class PostAdmin(LimitForeignKeyAdmin):
    prepopulated_fields = {'slug': ('headline', )}
    list_display = ('author', 'created', 'headline', 'published', )

    exclude = ('author', )

    form = PostAdminForm

    # -------------------------------------------------- Handle default values
    def add_view(self, request):
        if request.method == 'POST':
            request.POST['author'] = unicode(request.user.pk)
        return super(PostAdmin, self).add_view(request)

    def change_view(self, request, obj_id):
        if request.method == 'POST':
            old = Post.objects.get(id=obj_id)
            request.POST['author'] = old.author.pk
        return super(PostAdmin, self).change_view(request, obj_id)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'created', 'post', )


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
