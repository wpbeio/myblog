from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """post的表单"""
    class Meta(object):
        """docstring for Meta"""
        model = Post
        fields = ('title', 'text')
        labels = {
            'title': ('标题'),
            'text': ('正文'),
        }
