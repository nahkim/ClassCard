from django.shortcuts import render,redirect
from .models import ServiceQuestion,ServiceComment
from .forms import QuestionCreateForm, ServiceCommentCreateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from card.models import Card, CompareCard, Benefit
# Create your views here.

def index(request):
    # ======== nav바에 카드비교 카테고리 ========= 
    if request.user.is_authenticated:
        compare_cards = CompareCard.objects.filter(user=request.user)
    else:
        compare_cards = '로그인을 해야 카드 비교 기능을 사용하실 수 있습니다'

    questions = ServiceQuestion.objects.all()
    
    if request.method == 'GET':
        text = request.GET.get('search')
        if text :
            questions = ServiceQuestion.objects.filter(title__contains=text)

    page = int(request.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(questions, '5') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    context = {
        "compare_cards": compare_cards,
        'question_list' : page_obj,
    }
    return render(request, 'servicecenter/index.html', context)

@login_required(login_url='/login/')
def create(request):
    # ======== nav바에 카드비교 카테고리 ========= 
    if request.user.is_authenticated:
        compare_cards = CompareCard.objects.filter(user=request.user)
    else:
        compare_cards = '로그인을 해야 카드 비교 기능을 사용하실 수 있습니다'

    if request.method == 'POST':
        form = QuestionCreateForm(request.POST)
        if form.is_valid():
            serv_form = form.save(commit=False)
            serv_form.user = request.user
            serv_form.save()
            return redirect('service:index')
    else:
        form = QuestionCreateForm()
    context = {
        "compare_cards": compare_cards,
        'form' : form,
    }
    return render(request, 'servicecenter/create.html',context)

def detail(request,pk):
    # ======== nav바에 카드비교 카테고리 ========= 
    if request.user.is_authenticated:
        compare_cards = CompareCard.objects.filter(user=request.user)
    else:
        compare_cards = '로그인을 해야 카드 비교 기능을 사용하실 수 있습니다'
    
    question = ServiceQuestion.objects.get(pk=pk)
    comment = ServiceComment.objects.filter(quest_id=pk)
    if request.POST:
        comment_form = ServiceCommentCreateForm(request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.quest_id = pk
            form.user = request.user
            form.save()
            return redirect('service:detail', pk)
    else:
        comment_form = ServiceCommentCreateForm()

    context = {
        "compare_cards" : compare_cards,
        'question' : question,
        'comment_form' : comment_form,
        'comments':comment,
    }
    return render(request, 'servicecenter/detail.html', context)