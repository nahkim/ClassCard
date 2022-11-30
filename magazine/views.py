from django.shortcuts import render, redirect, get_object_or_404
from .models import Magazine, Comment
from .forms import MagazineForm, MagazineCommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
# Create your views here.

def index(request):
    # 인덱스에서 별점 평균 어떻게 산출할까요 나중에 데이터 넣고 고민해봅시다.
    magazines = Magazine.objects.all()
    
    context = {
        'magazines' : magazines,
    }
    return render(request, 'magazine/index.html', context)

# @login_required
def create_(request):
    # if request.user.role == 'column':
    if request.method == 'POST':
        magazine_form = MagazineForm(request.POST, request.FILES)
        if magazine_form.is_valid():
            magazine_form.save()
            return redirect('magazine:index')
    else:
        magazine_form = MagazineForm()

    context = {
        'magazine_form' : magazine_form,
    }
    # else: 
        # messages.warning(request,'쓰기 권한이 없습니다.')
    return render(request, 'magazine/create.html', context)

def detail(request,pk):
    magazine = Magazine.objects.get(pk=pk)
    mzcomment_form = MagazineCommentForm()
    mzcomments =magazine.comment_set.all()
    context = {
        'magazine' : magazine,
        'mzcomment_form' : mzcomment_form,
        'mzcomments' : mzcomments,
    }
    return render(request, 'magazine/detail.html', context)

# @login_required
def update_(request,pk):
    # if request.user.role == 'column':
    magazine = Magazine.objects.get(pk=pk)
    if request.method == 'POST':
        magazine_form = MagazineForm(request.POST, request.FILES, instance=magazine)
        if magazine_form.is_valid():
            # magazine_form.save(commit=False)
            # request.user = magazine.user:
            magazine_form.save()
            return redirect('magazine:index')
    else:
        magazine_form = MagazineForm(instance=magazine)
    # else: 
        # messages.warning(request,'쓰기 권한이 없습니다.')
    context = {
        'magazine_form' : magazine_form,
    }
    return render(request, 'magazine/create.html', context)

# @login_required
def delete_magazine(request, pk):
    magazine = Magazine.objects.get(pk=pk)
    # if request.user == magazine.user:
    if request.method == 'POST':
        magazine.delete()
    else:
        messages.warning(request, '비정상적인 접근')
        return redirect('magazine:detail', pk)
    # else:
    #     messages.warning(request, '작성자만 삭제 가능')
    #     return redirect('magazine:detail', pk)
    return redirect('magazine:index')

# @login_required
def mzcomment_create(request,pk):
    magazine =get_object_or_404(Magazine, pk=pk)
    if request.method == 'POST':
        form = MagazineCommentForm(request.POST)
        if form.is_valid():
            mzcomment_form = form.save(commit=False)
            mzcomment_form.magazine = magazine
            mzcomment_form.user = request.user
            mzcomment_form.save()
    else:
        messages.warning(request, '비정상적인 접근')
    
    return redirect('magazine:detail', pk)

# @login_required
def mzcomment_delete(request, mz_pk, mzcm_pk):
    magazine = Magazine.objects.get(pk=mz_pk)
    mzcomment = Comment.objects.get(pk=mzcm_pk)
    if request.user == mzcomment.user :
        mzcomment.magazine = magazine
        mzcomment.delete()
    else:
        messages.warning(request, '본인이 작성한 글만 삭제 가능합니다.')
    return redirect(request, 'magazine/detail.html', mz_pk)
    
    

    
            