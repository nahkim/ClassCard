from django.forms import ModelForm
from .models import DetailComment

class DetailCommentForm(ModelForm):
    class Meta:
        model = DetailComment
        fields = ["content", "rate"]

    def clean(self):
        cleaned_data = super().clean()
        # 처음 값이 들어왔다 는 검증 진행
        content = cleaned_data.get('content')
        rate = cleaned_data.get('rate')