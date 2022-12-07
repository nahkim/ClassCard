from django.shortcuts import render, redirect
from .models import Card, Benefit, DetailComment
from .forms import DetailCommentForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
import random
import json

benefit_all = ["혜택2" ,"혜택5" ,"혜택 프로모션" ,"할인" ,"수수료우대" ,"연회비지원" ,"무이자할부" ,"바우처" ,"무실적" ,"모든가맹점" ,"APP" ,"골프" ,"경기관람" ,"레저/스포츠" ,"영화" ,"영화/문화" ,"디지털구독" ,"테마파크" ,"음원사이트" ,"공연/전시" ,"문화센터" ,"게임" ,"고속버스" ,"렌탈" ,"호텔" ,"면세점" ,"리조트" ,"온라인 여행사" ,"여행/숙박" ,"여행사" ,"교통" ,"기차" ,"대중교통" ,"택시" ,"PAYCO" ,"네이버페이" ,"간편결제" ,"카카오페이" ,"삼성페이" ,"차/중고차" ,"충전소" ,"주유" ,"주유소" ,"렌터카" ,"정비" ,"하이패스" ,"자동차" ,"자동차/하이패스" ,"동물병원" ,"펫샵" ,"애완동물" ,"카페" ,"카페/디저트" ,"베이커리" ,"병원" ,"병원/약국" ,"약국" ,"피트니스" ,"드럭스토어" ,"보험" ,"보험사" ,"PAYCO" ,"네이버페이" ,"간편결제" ,"카카오페이" ,"삼성페이" ,"아이스크림" ,"패밀리레스토랑" ,"패스트푸드" ,"저녁" ,"점심" ,"푸드" ,"일반음식점" ,"배달앱" ,"CJ ONE" ,"OK캐쉬백" ,"해피포인트" ,"캐시백" ,"멤버십포인트" ,"적립" ,"BC TOP" ,"SSM" ,"금융" ,"증권사" ,"은행사" ,"KT" ,"LGU+" ,"SKT" ,"통신" ,"헤어" ,"화장품" ,"뷰티/피트니스" ,"대형마트" ,"해외직구" ,"아울렛" ,"홈쇼핑" ,"소셜커머스" ,"쇼핑" ,"백화점" ,"마트/편의점" ,"온라인쇼핑" ,"전통시장" ,"편의점" ,"공항" ,"공항라운지" ,"공항라운지/PP" ,"대한항공" ,"아시아나항공" ,"항공권" ,"항공마일리지" ,"제주항공" ,"저가항공" ,"진에어" ,"라운지키" ,"교육/육아" ,"도서" ,"학습지" ,"학원" ,"어린이집" ,"유치원" ,"SPA브랜드" ,"직장인" ,"비즈니스" ,"프리미엄" ,"프리미엄 서비스" ,"PP" ,"생활" ,"인테리어" ,"아이행복" ,"공과금" ,"공과금/렌탈" ,"국민행복" ,"해외" ,"해외이용" ,"지역" ,"카드사" ,"선택형" ,"하이브리드" ,"제휴/PLCC" ,"기타"]

# Create your views here.
benefit_dict = {
    "bene": ["혜택2", "혜택5", "혜택 프로모션", "할인", "수수료우대", "연회비지원", "무이자할부", "바우처", "무실적", "모든가맹점"],
    "sport": ["골프", "경기관람", "레저/스포츠"],
    "movie": [ "영화", "영화/문화", "디지털구독"],
    "culture": ["게임", "테마파크", "음원사이트", "문화센터", "공연/전시"],
    "travel": ["고속버스", "렌탈", "호텔", "면세점", "리조트", "온라인 여행사", "여행/숙박", "여행사"],
    "transport": ["교통", "기차", "대중교통", "택시"],
    "pay": ["PAYCO", "네이버페이", "간편결제", "카카오페이", "삼성페이"],
    "point": ["CJ ONE", "OK캐쉬백", "해피포인트", "캐시백", "멤버십포인트", "적립", "BC TOP", "SSM"],
    "tele": ["KT", "LGU+", "SKT", "통신"],
    "shop": ["대형마트", "해외직구", "아울렛", "홈쇼핑", "소셜커머스", "쇼핑", "백화점", "마트/편의점", "온라인쇼핑", "전통시장", "편의점"],
    "edu": ["교육/육아", "도서", "학습지", "학원", "어린이집", "유치원"],
    "business": ["직장인", "비즈니스"],
    "life": ["생활", "인테리어", "아이행복"],
    "gov": ["공과금", "공과금/렌탈", "국민행복"],
    "card_bene": ["카드사", "선택형", "하이브리드", "제휴/PLCC"],
    "app": ["APP"],
    "pet": ["동물병원", "펫샵", "애완동물"],
    "car": ["차/중고차", "충전소", "주유", "주유소", "렌터카", "정비", "하이패스", "자동차", "자동차/하이패스"],
    "cafe": ["카페", "카페/디저트", "베이커리"],
    "health": ["병원", "병원/약국", "약국", "피트니스", "드럭스토어"],
    "assurance": ["보험", "보험사"],
    "food": ["아이스크림", "패밀리레스토랑", "패스트푸드", "저녁", "점심", "푸드", "일반음식점", "배달앱"],
    "finance": ["금융", "증권사", "은행사"],
    "beauty": ["헤어", "화장품", "뷰티/피트니스"],
    "airplane": ["공항", "공항라운지", "공항라운지/PP", "대한항공", "아시아나항공", "항공권", "항공마일리지", "제주항공", "저가항공", "진에어", "라운지키"],
    "fashion": ["SPA브랜드"],
    "premium": ["프리미엄", "프리미엄 서비스", "PP"],
    "place": ["해외", "해외이용", "지역"],
    "etc": ["기타"],
    "note": ["유의사항"],
}

kor_benefit_dict_keys = ["혜택", "스포츠", "영화", "문화", "여행", "교통", "페이", "포인트", "통신사", "쇼핑", "교육", "비즈니스", "생활", "공과금", "카드", "어플", "애완동물", "자동차", "카페", "건강", "보험", "음식", "금융", "뷰티", "항공", "패션", "프리미엄", "지역", "기타", "유의사항"]

benefit_lst = benefit_dict.keys()
benefit_key = list(benefit_lst)


def detail(request, num):
    # 크롤링 할 때에 중간중간 없는 카드들이 있어서 id와 card_id가 다르다
    # 그래서 id가 아니라 card_id를 사용할 것 (id를 사용하면 혜택 부분이랑 꼬이게 된다)
    try:
        cards_all = Card.objects.all()
        card = Card.objects.get(card_id=num)
        benefit = Benefit.objects.filter(card_id=num)
        benefit_cate = []
        # benefit과 benfit_cate를 하나씩 튜플로 넣어서 저장하기
        # 탬플렛에서 사용하기 편하게
        bnf_list = []

        # 카드 10개를 랜덤으로 가지고오기 (배너)
        cards_random = random.sample(range(len(cards_all)), 10)

        for bnf in benefit:

            if bnf.bnf_name in benefit_dict["bene"]:
                benefit_cate.append("혜택")
            elif bnf.bnf_name in benefit_dict["sport"]:
                benefit_cate.append("스포츠")
            elif bnf.bnf_name in benefit_dict["movie"]:
                benefit_cate.append("영화")
            elif bnf.bnf_name in benefit_dict["culture"]:
                benefit_cate.append("문화")
            elif bnf.bnf_name in benefit_dict["travel"]:
                benefit_cate.append("여행")
            elif bnf.bnf_name in benefit_dict["transport"]:
                benefit_cate.append("교통")
            elif bnf.bnf_name in benefit_dict["pay"]:
                benefit_cate.append("페이")
            elif bnf.bnf_name in benefit_dict["point"]:
                benefit_cate.append("포인트")
            elif bnf.bnf_name in benefit_dict["tele"]:
                benefit_cate.append("통신사")
            elif bnf.bnf_name in benefit_dict["shop"]:
                benefit_cate.append("쇼핑")
            elif bnf.bnf_name in benefit_dict["edu"]:
                benefit_cate.append("교육")
            elif bnf.bnf_name in benefit_dict["business"]:
                benefit_cate.append("비즈니스")
            elif bnf.bnf_name in benefit_dict["life"]:
                benefit_cate.append("생활")
            elif bnf.bnf_name in benefit_dict["gov"]:
                benefit_cate.append("공과금")
            elif bnf.bnf_name in benefit_dict["card_bene"]:
                benefit_cate.append("카드")
            elif bnf.bnf_name in benefit_dict["app"]:
                benefit_cate.append("어플")
            elif bnf.bnf_name in benefit_dict["pet"]:
                benefit_cate.append("애완동물")
            elif bnf.bnf_name in benefit_dict["car"]:
                benefit_cate.append("자동차")
            elif bnf.bnf_name in benefit_dict["cafe"]:
                benefit_cate.append("카페")
            elif bnf.bnf_name in benefit_dict["health"]:
                benefit_cate.append("건강")
            elif bnf.bnf_name in benefit_dict["assurance"]:
                benefit_cate.append("보험")
            elif bnf.bnf_name in benefit_dict["food"]:
                benefit_cate.append("음식")
            elif bnf.bnf_name in benefit_dict["finance"]:
                benefit_cate.append("금융")
            elif bnf.bnf_name in benefit_dict["beauty"]:
                benefit_cate.append("뷰티")
            elif bnf.bnf_name in benefit_dict["airplane"]:
                benefit_cate.append("항공")
            elif bnf.bnf_name in benefit_dict["fashion"]:
                benefit_cate.append("패션")
            elif bnf.bnf_name in benefit_dict["premium"]:
                benefit_cate.append("프리미엄")
            elif bnf.bnf_name in benefit_dict["place"]:
                benefit_cate.append("지역")
            elif bnf.bnf_name in benefit_dict["etc"]:
                benefit_cate.append("기타")
            elif bnf.bnf_name in benefit_dict["note"]:
                benefit_cate.append("유의사항")

        for j in range(len(benefit)):
            bnf_list.append((benefit[j], benefit_cate[j]))

        detail_comment_form = DetailCommentForm()

        detail_comments = card.detailcomment_set.all().order_by("-updated_at")

        detail_comments_num = card.detailcomment_set.all().count

        context = {
            # 카드 배너
            "cards_random1": cards_all[cards_random[0]],
            "cards_random2": cards_all[cards_random[1]],
            "cards_random3": cards_all[cards_random[2]],
            "cards_random4": cards_all[cards_random[3]],
            "cards_random5": cards_all[cards_random[4]],
            "cards_random6": cards_all[cards_random[5]],
            "cards_random7": cards_all[cards_random[6]],
            "cards_random8": cards_all[cards_random[7]],
            "cards_random9": cards_all[cards_random[8]],
            "cards_random10": cards_all[cards_random[9]],
            "card_id": card.card_id,
            "card_img": card.card_img,
            "card_name": card.card_name,
            # 카드사
            "card_brand": card.card_brand,
            # 국내 해외 전용
            "card_in_out_1": card.card_in_out_1,
            "card_in_out_2": card.card_in_out_2,
            "card_in_out_3": card.card_in_out_3,
            # 전월실적
            "card_record": card.card_record,
            # 연동 해외 카드
            "card_overseas": card.card_overseas,
            # ===== 주요 혜택 ========
            "benefit_count": range(len(benefit)),
            "benefits": bnf_list,
            # ========= 댓글 관련 =======
            "detail_comment_form": detail_comment_form,
            "detail_comments": detail_comments,
            "detail_comments_num": detail_comments_num,
        }

    except:
        return redirect("main")

    return render(request, "card/detail.html", context)

@login_required
def comment(request, pk):
    card = Card.objects.get(card_id=pk)
    user = request.user.pk

    if request.method == "POST":
        comment_form = DetailCommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.card = card
            comment.user = request.user
            comment.save()

    comments = DetailComment.objects.all().order_by('-updated_at')
    comment_data = []

    for comment in comments:
        comment_data.append({
            'user_id' : comment.user.id,
            'comment_id': comment.id,
            'userName': comment.user.username,
            'rate' : comment.rate,
            'content' : comment.content,
            'update' : comment.updated_at,
        })
    
    data = {
        'commentData' : comment_data,
        'user' : user,
        'cardId' : card.card_id,
    }

    return JsonResponse(data)


def comment_delete(request, card_id, comment_pk):
    card = Card.objects.get(card_id=card_id)
    comment = DetailComment.objects.get(pk = comment_pk)
    user = request.user.pk

    comment.delete()

    comments = DetailComment.objects.all().order_by('-updated_at')
    comment_data = []

    for comment in comments:
        comment_data.append({
            'user_id' : comment.user.id,
            'comment_id': comment.id,
            'userName': comment.user.username,
            'rate' : comment.rate,
            'content' : comment.content,
            'update' : comment.updated_at,
        })
    
    data = {
        'commentData' : comment_data,
        'user' : user,
        'cardId' : card.card_id,
    }

    return JsonResponse(data)

def comment_update(request, card_id, comment_pk):
    card = Card.objects.get(card_id=card_id)
    comment = DetailComment.objects.get(pk=comment_pk)
    user = request.user.pk

    jsonObject = json.loads(request.body)

    if request.method == 'POST':
        comment.content = jsonObject.get('content')
        comment.rate = jsonObject.get('rate')
        comment.save()

    comments = DetailComment.objects.all().order_by('-updated_at')
    comment_data = []

    for comment in comments:
        comment_data.append({
            'user_id' : comment.user.id,
            'comment_id': comment.id,
            'userName': comment.user.username,
            'rate' : comment.rate,
            'content' : comment.content,
            'update' : comment.updated_at,
        })
    
    data = {
        'commentData' : comment_data,
        'user' : user,
        'cardId' : card.card_id,
    }

    return JsonResponse(data)

from django.core.paginator import Paginator, PageNotAnInteger

card_list = []
def search(request):
    global card_list

    if request.method == "GET":
        card_list = []
        cards = Card.objects.exclude(card_name = None)
        
        #============================ 체크 카드랑 신용카드 분리 하기 ===========================

        check_card = []
        credit_card = []

        for card in cards:
            if "체크" in card.card_name:
                check_card.append(card)
            else:
                credit_card.append(card)

        #==========================================================

        age = request.GET.get("age", "")
        card_type = request.GET.get("type", "")
        # korean benefit list
        kbl = request.GET.getlist("answers", "")

        # ============================ 나이와 카드 종류로 필터링 하기 ==========================================
        if age == "20대":
            age_20 = ["혜택2" ,"혜택5" ,"혜택 프로모션" ,"할인" ,"수수료우대" ,"연회비지원" ,"무이자할부" ,"바우처" ,"무실적" ,"모든가맹점" ,"APP" ,"골프" ,"경기관람" ,"레저/스포츠" ,"영화" ,"영화/문화" ,"디지털구독" ,"테마파크" ,"음원사이트" ,"공연/전시" ,"게임" ,"고속버스" ,"렌탈" ,"면세점", "온라인 여행사" ,"여행/숙박" ,"여행사" ,"교통" ,"기차" ,"대중교통", "PAYCO" ,"네이버페이" ,"간편결제" ,"카카오페이" ,"삼성페이", "동물병원" ,"펫샵" ,"애완동물" ,"카페" ,"카페/디저트" , "베이커리", "피트니스" , "PAYCO" ,"네이버페이" ,"간편결제" ,"카카오페이" ,"삼성페이" ,"아이스크림", "패스트푸드" ,"저녁" ,"점심" ,"푸드" ,"일반음식점" ,"배달앱" ,"CJ ONE" ,"OK캐쉬백" ,"해피포인트" ,"캐시백" ,"멤버십포인트" ,"적립" ,"BC TOP" ,"SSM" , "KT" ,"LGU+" ,"SKT" ,"통신" ,"헤어" ,"화장품" ,"뷰티/피트니스", "해외직구" ,"아울렛", "소셜커머스" ,"쇼핑" ,"백화점" ,"마트/편의점" ,"온라인쇼핑","편의점" , "공항", "대한항공", "아시아나항공" ,"항공권" ,"항공마일리지" ,"제주항공" ,"저가항공" ,"진에어", "도서", "SPA브랜드" ,"직장인" ,"비즈니스" ,"해외" ,"해외이용" ,"지역" ,"카드사" ,"선택형" ,"하이브리드" ,"제휴/PLCC" ,"기타"]
            
            # ================ 카드 혜택 필터링도 입력 했을 때 ==================
            if kbl: 
                bnf_list = []

                for k in kbl:
                    bene_index = kor_benefit_dict_keys.index(k)
                    bnfs = benefit_dict[benefit_key[bene_index]]

                    for bnf in bnfs:
                        if bnf in age_20:
                            bnf_list.append(bnf)
                
                if card_type == "체크":
                    for check in check_card:
                        benefits_temp = Benefit.objects.filter(card_id = check.card_id)
                        
                        for benefit in benefits_temp:
                            if benefit.bnf_name in bnf_list:
                                card_list.append(check)
                                break
                
                else:
                    for credit in credit_card:
                        benefits_temp = Benefit.objects.filter(card_id = credit.card_id)
                        
                        for benefit in benefits_temp:
                            if benefit.bnf_name in bnf_list:
                                card_list.append(check)
                                break
        
            print(card_list)

        elif age == "30대":
            age_30 = ["혜택2" ,"혜택5" ,"혜택 프로모션" ,"할인" ,"수수료우대" ,"연회비지원" ,"무이자할부" ,"바우처" ,"무실적" ,"모든가맹점" ,"APP" ,"골프" ,"경기관람" ,"레저/스포츠" ,"영화" ,"영화/문화" ,"디지털구독" ,"음원사이트" ,"공연/전시","렌탈" ,"호텔" ,"면세점" ,"리조트" ,"온라인 여행사" ,"여행/숙박" ,"여행사" ,"교통" ,"기차" ,"대중교통" ,"택시" ,"PAYCO" ,"네이버페이" ,"간편결제" ,"카카오페이" ,"삼성페이" ,"차/중고차" ,"충전소" ,"주유" ,"주유소" ,"렌터카" ,"정비" ,"하이패스" ,"자동차" ,"자동차/하이패스" ,"동물병원" ,"펫샵" ,"애완동물" ,"카페" ,"카페/디저트" ,"베이커리" ,"병원" ,"병원/약국" ,"약국" ,"피트니스" ,"드럭스토어" ,"보험" ,"보험사" ,"PAYCO" ,"네이버페이" ,"간편결제" ,"카카오페이" ,"삼성페이" ,"아이스크림" ,"패밀리레스토랑", "저녁" ,"점심" ,"푸드" ,"일반음식점" ,"배달앱" ,"CJ ONE" ,"OK캐쉬백" ,"해피포인트" ,"캐시백" ,"멤버십포인트" ,"적립" ,"BC TOP" ,"SSM" ,"금융" ,"증권사" ,"은행사" ,"KT" ,"LGU+" ,"SKT" ,"통신" ,"헤어" ,"화장품" ,"뷰티/피트니스" ,"대형마트" ,"해외직구" ,"아울렛" ,"소셜커머스" ,"쇼핑" ,"백화점","온라인쇼핑", "편의점" ,"공항", "대한항공" ,"아시아나항공" ,"항공권" ,"항공마일리지" ,"제주항공" ,"저가항공" ,"진에어", "교육/육아" ,"도서" ,"학습지" ,"학원" ,"어린이집" ,"유치원" ,"SPA브랜드" ,"직장인" ,"비즈니스", "생활" ,"인테리어" ,"아이행복" ,"공과금" ,"공과금/렌탈" ,"국민행복" ,"해외" ,"해외이용" ,"지역" ,"카드사" ,"선택형" ,"하이브리드" ,"제휴/PLCC" ,"기타"]
            
            # ================ 카드 혜택 필터링도 입력 했을 때 ==================
            if kbl: 
                bnf_list = []

                for k in kbl:
                    bene_index = kor_benefit_dict_keys.index(k)
                    bnfs = benefit_dict[benefit_key[bene_index]]

                    for bnf in bnfs:
                        if bnf in age_30:
                            bnf_list.append(bnf)

                if card_type == "체크":
                    for check in check_card:
                        benefits_temp = Benefit.objects.filter(card_id = check.card_id)
                        
                        for benefit in benefits_temp:
                            if benefit.bnf_name in bnf_list:
                                card_list.append(check)
                                break
                
                else:
                    for credit in credit_card:
                        benefits_temp = Benefit.objects.filter(card_id = credit.card_id)
                        
                        for benefit in benefits_temp:
                            if benefit.bnf_name in bnf_list:
                                card_list.append(check)
                                break

        else:
            age_40 = ["혜택2" ,"혜택5" ,"혜택 프로모션" ,"할인" ,"수수료우대" ,"연회비지원" ,"무이자할부" ,"바우처" ,"무실적" ,"모든가맹점" ,"APP" ,"골프" ,"경기관람" ,"레저/스포츠" ,"영화" ,"영화/문화" ,"디지털구독" ,"음원사이트" ,"공연/전시" ,"문화센터","렌탈" ,"호텔" ,"면세점" ,"리조트" ,"온라인 여행사" ,"여행/숙박" ,"여행사" ,"교통" ,"기차" ,"대중교통" ,"택시" ,"PAYCO" ,"네이버페이" ,"간편결제" ,"카카오페이" ,"삼성페이" ,"차/중고차" ,"충전소" ,"주유" ,"주유소" ,"렌터카" ,"정비" ,"하이패스" ,"자동차" ,"자동차/하이패스" ,"동물병원" ,"펫샵" ,"애완동물","베이커리" ,"병원" ,"병원/약국" ,"약국" ,"피트니스" ,"드럭스토어" ,"보험" ,"보험사" ,"PAYCO" ,"네이버페이" ,"간편결제" ,"카카오페이" ,"삼성페이" ,"아이스크림" ,"패밀리레스토랑", "저녁" ,"점심" ,"푸드" ,"일반음식점" ,"CJ ONE" ,"OK캐쉬백" ,"해피포인트" ,"캐시백" ,"멤버십포인트" ,"적립" ,"BC TOP" ,"SSM" ,"금융" ,"증권사" ,"은행사" ,"KT" ,"LGU+" ,"SKT" ,"통신" ,"헤어" ,"화장품" ,"뷰티/피트니스" ,"대형마트", "아울렛", "홈쇼핑", "쇼핑" ,"백화점", "온라인쇼핑" ,"전통시장" ,"편의점" ,"공항" ,"공항라운지" ,"공항라운지/PP" ,"대한항공" ,"아시아나항공" ,"항공권" ,"항공마일리지" ,"제주항공" ,"저가항공" ,"진에어" ,"라운지키" ,"교육/육아" ,"도서" ,"학습지" ,"학원" ,"어린이집" ,"유치원" ,"SPA브랜드" ,"직장인" ,"비즈니스" ,"프리미엄" ,"프리미엄 서비스" ,"PP" ,"생활" ,"인테리어" ,"아이행복" ,"공과금" ,"공과금/렌탈" ,"국민행복" ,"해외" ,"해외이용" ,"지역" ,"카드사" ,"선택형" ,"하이브리드" ,"제휴/PLCC" ,"기타"]
            
            # ================ 카드 혜택 필터링도 입력 했을 때 ==================
            if kbl: 
                bnf_list = []

                for k in kbl:
                    bene_index = kor_benefit_dict_keys.index(k)
                    bnfs = benefit_dict[benefit_key[bene_index]]

                    for bnf in bnfs:
                        if bnf in age_40:
                            bnf_list.append(bnf)

                if card_type == "체크":
                        for check in check_card:
                            benefits_temp = Benefit.objects.filter(card_id = check.card_id)
                            
                            for benefit in benefits_temp:
                                if benefit.bnf_name in bnf_list:
                                    card_list.append(check)
                                    break
                    
                else:
                    for credit in credit_card:
                        benefits_temp = Benefit.objects.filter(card_id = credit.card_id)
                        
                        for benefit in benefits_temp:
                            if benefit.bnf_name in bnf_list:
                                card_list.append(check)
                                break

        page = 1
        paginator = Paginator(card_list, 10)
        try:
            paged_list = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            paged_list = paginator.page(page)

    else:
        page = request.GET.get('page')
        paginator = Paginator(card_list, 10)
        try:
            paged_list = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            paged_list = paginator.page(page)
        
    context = {
        "kor_benefit_lst": kor_benefit_dict_keys,
        "benefit_card_list": paged_list,   
        "card_lst" : card_list,
        "age_param": age,
        "card_type_param": card_type, 
        "kbl_param": ','.join(kbl),
    }
    return render(request, "card/search.html", context)
