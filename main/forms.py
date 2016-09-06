from django.forms import ModelForm
from models import CommentTree


class CommentTreeForm(ModelForm):
    class Meta:
        model = CommentTree
        fields = ['text', 'parent', 'id']
