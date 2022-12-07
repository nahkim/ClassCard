from django import forms
from .models import ServiceQuestion,ServiceComment

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = ServiceQuestion
        fields = ('title','content',)
        

class ServiceCommentCreateForm(forms.ModelForm):
    class Meta:
        model = ServiceComment
        fields = ('content',)
        widgets = {
            'content':forms.Textarea(attrs={'style':'height:100px'})
        }
             