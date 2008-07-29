from django import forms


from models import Post, PostComment


class AddPostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('author_name', 'author_url', 'copy')


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', )


"""
def article_restricted_form_factory(categories_qs):
    class ArticleRestrictedForm(forms.ModelForm):
        author = forms.ModelChoiceField(queryset=authors)

        class Meta:
            model = models.Article
            if len(categories) <= 1:
                exclude = ('author', )

    return ArticleRestrictedForm
"""
