from django.forms import ModelForm
from .models import Magazine, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class MagazineForm(ModelForm):
    class Meta:
        model = Magazine
        fields = ('title', 'sub_title', 'content','tag')
        widgets = {
            'content': SummernoteWidget(),
        }

class MagazineCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content','grade',)