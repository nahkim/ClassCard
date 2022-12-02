from django.forms import ModelForm
from .models import Magazine, Comment

class MagazineForm(ModelForm):
    class Meta:
        model = Magazine
        fields = ('title', 'content', 'image','sub_title')

class MagazineCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content','grade',)