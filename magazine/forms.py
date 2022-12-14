from django.forms import ModelForm, NumberInput
from .models import Magazine, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class MagazineForm(ModelForm):
    class Meta:
        model = Magazine
        fields = ('title', 'sub_title', 'content','image')
        widgets = {
            'content': SummernoteWidget(),
        }
        label={
            'image':'썸네일 이미지',
        }

class MagazineCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content','grade',)
        widgets = {
            'grade' : NumberInput(attrs={'min':'1','max':'5'}) 
        }