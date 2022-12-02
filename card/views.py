from django.shortcuts import render, redirect
from .models import Card, Benefit
from django.contrib import messages
import random

# Create your views here.
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

def detail(request, num):
    # 크롤링 할 때에 중간중간 없는 카드들이 있어서 id와 card_id가 다르다
    # 그래서 id가 아니라 card_id를 사용할 것 (id를 사용하면 혜택 부분이랑 꼬이게 된다)
    try:
        cards_all = Card.objects.all()
        card = Card.objects.get(card_id = num)
        benefit = Benefit.objects.filter(card_id = num)
        benefit_cate = []
        # benefit과 benfit_cate를 하나씩 튜플로 넣어서 저장하기
        # 탬플렛에서 사용하기 편하게
        bnf_list = []

        # 카드 10개를 랜덤으로 가지고오기 (배너)
        cards_random = random.sample(range(len(cards_all)), 10)
         
        for bnf in benefit:

            if bnf.bnf_name in benefit_dict['bene']:
                benefit_cate.append('혜택')
            elif bnf.bnf_name in benefit_dict['sport']:
                benefit_cate.append('스포츠')
            elif bnf.bnf_name in benefit_dict['movie']:
                benefit_cate.append('영화')
            elif bnf.bnf_name in benefit_dict['culture']:
                benefit_cate.append('문화')
            elif bnf.bnf_name in benefit_dict['travel']:
                benefit_cate.append('여행')
            elif bnf.bnf_name in benefit_dict['transport']:
                benefit_cate.append('교통')
            elif bnf.bnf_name in benefit_dict['pay']:
                benefit_cate.append('페이')
            elif bnf.bnf_name in benefit_dict['point']:
                benefit_cate.append('포인트')
            elif bnf.bnf_name in benefit_dict['tele']:
                benefit_cate.append('통신사')
            elif bnf.bnf_name in benefit_dict['shop']:
                benefit_cate.append('쇼핑')
            elif bnf.bnf_name in benefit_dict['edu']:
                benefit_cate.append('교육')
            elif bnf.bnf_name in benefit_dict['business']:
                benefit_cate.append('비즈니스')
            elif bnf.bnf_name in benefit_dict['life']:
                benefit_cate.append('생활')
            elif bnf.bnf_name in benefit_dict['gov']:
                benefit_cate.append('공과금')
            elif bnf.bnf_name in benefit_dict['card_bene']:
                benefit_cate.append('카드')
            elif bnf.bnf_name in benefit_dict['app']:
                benefit_cate.append('어플')
            elif bnf.bnf_name in benefit_dict['pet']:
                benefit_cate.append('애완동물')
            elif bnf.bnf_name in benefit_dict['car']:
                benefit_cate.append('자동차')
            elif bnf.bnf_name in benefit_dict['cafe']:
                benefit_cate.append('카페')
            elif bnf.bnf_name in benefit_dict['health']:
                benefit_cate.append('건강')
            elif bnf.bnf_name in benefit_dict['assurance']:
                benefit_cate.append('보험')
            elif bnf.bnf_name in benefit_dict['food']:
                benefit_cate.append('음식')
            elif bnf.bnf_name in benefit_dict['finance']:
                benefit_cate.append('금융')
            elif bnf.bnf_name in benefit_dict['beauty']:
                benefit_cate.append('뷰티')
            elif bnf.bnf_name in benefit_dict['airplane']:
                benefit_cate.append('항공')
            elif bnf.bnf_name in benefit_dict['fashion']:
                benefit_cate.append('패션')
            elif bnf.bnf_name in benefit_dict['premium']:
                benefit_cate.append('프리미엄')
            elif bnf.bnf_name in benefit_dict['place']:
                benefit_cate.append('지역')
            elif bnf.bnf_name in benefit_dict['etc']:
                benefit_cate.append('기타')
            elif bnf.bnf_name in benefit_dict['note']:
                benefit_cate.append('유의사항')

        for j in range(len(benefit)):
            bnf_list.append((benefit[j], benefit_cate[j]))

        context = {
            # 카드 배너
            'cards_random1' : cards_all[cards_random[0]],
            'cards_random2' : cards_all[cards_random[1]],
            'cards_random3' : cards_all[cards_random[2]],
            'cards_random4' : cards_all[cards_random[3]],
            'cards_random5' : cards_all[cards_random[4]],
            'cards_random6' : cards_all[cards_random[5]],
            'cards_random7' : cards_all[cards_random[6]],
            'cards_random8' : cards_all[cards_random[7]],
            'cards_random9' : cards_all[cards_random[8]],
            'cards_random10' : cards_all[cards_random[9]],


            'card_img' : card.card_img,
            'card_name' : card.card_name,
            # 카드사
            'card_brand' : card.card_brand,
            # 국내 해외 전용  
            'card_in_out_1' : card.card_in_out_1,
            'card_in_out_2' : card.card_in_out_2,
            'card_in_out_3' : card.card_in_out_3,
            # 전월실적
            'card_record' : card.card_record,
            # 연동 해외 카드
            'card_overseas' : card.card_overseas,
            # ===== 주요 혜택 ========
            'benefit_count' : range(len(benefit)),
            'benefits' : bnf_list, 
        }

        print(bnf_list[0][0].bnf_detail, type(bnf_list[0][0].bnf_detail))

    except:
        return redirect('main')
        
    return render(request, 'card/detail.html', context)

def search(request):

    global benefit_key
    global kor_benefit_dict_keys
    
    if request.method == 'GET':
        kbl = request.GET.get('benefit','')

        if kbl:
            index = kor_benefit_dict_keys.index(kbl)
            benefit_key = benefit_key[index]
            # 키 값으로 딕셔너리 값 찾아가기
            benefit_list = benefit_dict[benefit_key]
            # 값리스트에 포함되는 혜택 필터링
            benefit_card_lst = Benefit.objects.filter(bnf_name__in=benefit_list)
            # card_id 추출, 중복제거
            benefit_card_lst_d = benefit_card_lst.values('card_id').distinct()
            # print(type(benefit_card_lst_d))
            # 카드id로 카드 리스트 필터링
            card_list = Card.objects.filter(card_id__in=benefit_card_lst_d)
            context = {
                'benefit_lst' : benefit_lst,
                'kor_benefit_lst' : kor_benefit_dict_keys,
                'benefit_card_list' : card_list,
            }
        else:
            context = {
                'kor_benefit_lst' : kor_benefit_dict_keys,
            }
    

    return render(request, 'card/search.html', context)