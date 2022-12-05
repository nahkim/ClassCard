from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login


@require_http_methods(["GET", "POOST"])
def signup(request):
    if request.user.is_authenticated:
        messages.warning(request, "이미 로그인 중입니다.")
        return redirect("main")
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "가입이 완료되었습니다.")
            return redirect("main")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)

@require_http_methods(["GET", "POOST"])
def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "이미 로그인 중입니다.")
        return redirect("main")
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(request.GET.get("next") or "main")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

