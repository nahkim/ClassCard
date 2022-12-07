from django.shortcuts import render,redirect
from .models import ServiceQuestion,ServiceComment
from .forms import QuestionCreateForm, ServiceCommentCreateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    questions = ServiceQuestion.objects.all()
    if request.method == 'GET':
        text = request.GET.get('search')
        if text :
            questions = ServiceQuestion.objects.filter(title__contains=text)
    context = {
        'questions' : questions,
    }
    return render(request, 'servicecenter/index.html', context)

@login_required(login_url='/login')
def create(request):
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
        'form' : form,
    }
    return render(request, 'servicecenter/create.html',context)

def detail(request,pk):
    
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
        'question' : question,
        'comment_form' : comment_form,
        'comments':comment,
    }
    return render(request, 'servicecenter/detail.html', context)