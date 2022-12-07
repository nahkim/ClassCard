from django.shortcuts import render, redirect, get_object_or_404
from .models import Magazine, Comment
from .forms import MagazineForm, MagazineCommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponseForbidden
# Create your views here.

def index(request):
    # 인덱스에서 별점 평균 어떻게 산출할까요 나중에 데이터 넣고 고민해봅시다.
    magazines = Magazine.objects.all()
    mz_year = Magazine.objects.filter(tag__contains='YEAR')
    mz_news = Magazine.objects.filter(tag__contains='NEWS')
    mz_recommend = Magazine.objects.filter(tag__contains='RECOMMEND')
    mz_basic = Magazine.objects.filter(tag__contains='BASIC')
    mz_bodo = Magazine.objects.filter(tag__contains='BODO')
    context = {
        'magazines' : magazines,
        'mz_year' : mz_year,
        'mz_news' : mz_news,
        'mz_recommend' : mz_recommend,
        'mz_basic' : mz_basic,
        'mz_bodo' : mz_bodo,
    }
    return render(request, 'magazine/index.html', context)
    
# admin에서 사용자들 -> 사용자 이름 클릭 -> role 변경(필수항목 점검)
@login_required(login_url='/login/')
def create_(request):
    if request.user.role == 'C':
        if request.method == 'POST':
            form = MagazineForm(request.POST, request.FILES)
            if form.is_valid():
                magazine_form = form.save(commit=False)
                magazine_form.user = request.user
                magazine_form.save()
                return redirect('magazine:index')
        else:
            form = MagazineForm()
        context = {
            'magazine_form' : form,
        }
        return render(request, 'magazine/create.html', context)
    else: 
        messages.warning(request,'쓰기 권한이 없습니다.')
        return redirect('magazine:index')

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

@login_required
def update_(request,pk):
    magazine = Magazine.objects.get(pk=pk)
    if request.method == 'POST':
        magazine_form = MagazineForm(request.POST, request.FILES, instance=magazine)
        if magazine_form.is_valid():
            form = magazine_form.save(commit=False)
            request.user = form.user
            form.save()
            return redirect('magazine:detail',pk)
    else:
        magazine_form = MagazineForm(instance=magazine)
    context = {
        'magazine_form' : magazine_form,
    }
    return render(request, 'magazine/create.html', context)


@login_required
def delete_magazine(request, pk):
    magazine = Magazine.objects.get(pk=pk)
    if request.user == magazine.user:
        if request.method == 'POST':
            magazine.delete()
            return redirect('magazine:index')
        else:
            messages.warning(request, '비정상적인 접근')
            return redirect('magazine:detail', pk)
    else:
        messages.warning(request, '작성자만 삭제 가능')
        return redirect('magazine:detail', pk)

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
        return redirect("magazine:detail", mz_pk)
    else:
        return HttpResponseForbidden()
    

    
            