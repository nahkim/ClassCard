from django.shortcuts import render
from django.views.decorators.http import require_safe

benefit_dict = {
    'bene' : ['혜택2', '혜택5', '혜택 프로모션', '할인', '수수료우대', '연회비지원', '무이자할부', '바우처', '무실적', '모든가맹점'],
    'sport' : ['골프', '경기관람', '레저/스포츠'],
    'movie' : ['영화', '영화/문화', '디지털구독',],
    'culture': ['게임', '테마파크', '음원사이트', '문화센터', '공연/전시'],
    'travel' : ['고속버스', '렌탈', '호텔', '면세점', '리조트', '온라인 여행사', '여행/숙박', '여행사'],
    'transport' : ['교통', '기차', '대중교통', '택시'],
    'pay' : ['PAYCO', '네이버페이', '간편결제', '카카오페이', '삼성페이'],
    'point' : ['CJ ONE', 'OK캐쉬백', '해피포인트', '캐시백', '멤버십포인트', '적립', 'BC TOP', 'SSM'],
    'tele' : ['KT', 'LGU+', 'SKT', '통신'],
    'shop' : ['대형마트', '해외직구', '아울렛', '홈쇼핑', '소셜커머스', '쇼핑', '백화점', '마트/편의점', '온라인쇼핑', '전통시장', '편의점'],
    'edu' : ['교육/육아', '도서', '학습지', '학원', '어린이집', '유치원'],
    'business' : ['직장인', '비즈니스'],
    'life' : ['생활', '인테리어', '아이행복'],
    'gov' : ['공과금', '공과금/렌탈', '국민행복'],
    'card_bene' : ['카드사', '선택형', '하이브리드', '제휴/PLCC'],
    'app' : ['APP'],
    'pet' : ['동물병원', '펫샵', '애완동물'],
    'car' : ['차/중고차', '충전소', '주유', '주유소', '렌터카', '정비', '하이패스', '자동차', '자동차/하이패스'],
    'cafe' : ['카페', '카페/디저트', '베이커리'],
    'health' : ['병원', '병원/약국', '약국', '피트니스', '드럭스토어'],
    'assurance' : ['보험', '보험사'],
    'food' : ['아이스크림', '패밀리레스토랑', '패스트푸드', '저녁', '점심', '푸드', '일반음식점', '배달앱'],
    'finance' : ['금융', '증권사', '은행사'],
    'beauty' : ['헤어', '화장품', '뷰티/피트니스'],
    'airplane' : ['공항', '공항라운지', '공항라운지/PP', '대한항공', '아시아나항공', '항공권', '항공마일리지', '제주항공', '저가항공', '진에어', '라운지키'],
    'fashion' : ['SPA브랜드'],
    'premium' : ['프리미엄', '프리미엄 서비스', 'PP'],
    'place' : ['해외', '해외이용', '지역'],
    'etc' : ['기타'],
    'note' : ['유의사항'],
}
kor_benefit_dict_keys = ['혜택', '스포츠', '영화', '문화', '여행','교통','페이','포인트','통신사','쇼핑','교육','비즈니스','생활','공과금','카드','어플','애완동물','자동차','카페','건강','보험','음식','금융','뷰티','항공','패션','프리미엄','지역','기타','유의사항']

benefit_lst = benefit_dict.keys()
benefit_key = list(benefit_lst)

@require_safe
def main(request):

    # 애완동물을 위한 카드


    return render(request, "main.html")

# nav 검색기능(프로젝트 전체)
from django.db.models import Q
from card.models import Card, Benefit
from magazine.models import Magazine

def nav_search(request):
    if request.method == 'GET':
        text = request.GET.get('text')
        card_list = Card.objects.filter(Q(card_name__icontains=text)|Q(card_brand__icontains=text)|Q(card_in_out_1__contains=text)|Q(card_in_out_2__icontains=text)|Q(card_in_out_3__icontains=text)|Q(card_overseas__icontains=text)).distinct()
        
        
        # 카드 id 필드 사라짐. 보류
        # benefit_list = Benefit.objects.filter(Q(bnf_name__icontains=text)|Q(bnf_content__icontains=text)|Q(bnf_detail__icontains=text))
        # benefit_card_lst = benefit_list.values('card_id').distinct()

        # 매거진
        magazin_list = Magazine.objects.filter(Q(title__icontains=text)|Q(content__icontains=text)).distinct()
        context = {
            'text' : text,
            'card_list' : card_list,
            # 'benefit_card_lst' : benefit_list,
            'magazine_list' : magazin_list,
        }
        return render(request, 'nav_search.html',context)