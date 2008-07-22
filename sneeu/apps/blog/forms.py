from django import newforms as forms


class AddPostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('author_name', 'author_url', 'copy')
