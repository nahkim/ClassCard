from django.shortcuts import render
from card.models import CompareCard, Card, Benefit

# Create your views here.
def eventhome(request):
    # ======== nav바에 카드비교 카테고리 ========= 
    if request.user.is_authenticated:
        compare_cards = CompareCard.objects.filter(user=request.user)
    else:
        compare_cards = '로그인을 해야 카드 비교 기능을 사용하실 수 있습니다'

    context = {
        "compare_cards" : compare_cards,
    }

    return render(request,'articles/eventhome.html', context)