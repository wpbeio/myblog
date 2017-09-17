from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """post的表单"""
    class Meta(object):
        """docstring for Meta"""
        model = Post
        fields = ('title', 'content','tags','category')

        labels = {
            'title': ('标题'),
            'content': ('正文'),
            'category': ('分类'),
            'tags': ('标签'),
        }
