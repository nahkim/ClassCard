from .models import DetailComment
from django import forms

class DetailCommentForm(forms.ModelForm):
    class Meta:
        model = DetailComment
        fields = ["content"]