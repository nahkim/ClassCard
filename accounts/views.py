from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse


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

# @require_safe
# def profile(request, username):
#     # get_user_model 확인
#     user = get_object_or_404(get_user_model(), username=username)
#     like_articles = user.like_articles.all()
#     following_users = user.followings.all()
#     context = {
#         "user": user,
#         "like_articles": like_articles,
#         "following_users": following_users,
#     }
#     return render(request, "accounts/profile.html", context)

# @require_POST
# def follow(request, username):
#     if not request.user.is_authenticated:
#         messages.warning(request, "로그인이 필요합니다.")
#         # 확인
#         return redirect("login")

#     user = get_object_or_404(get_user_model(), username=username)
#     if user != request.user:
#         if user.followers.filter(username=request.user.username).exists():
#             user.followers.remove(request.user)
#             is_followed = False
#         else:
#             user.followers.add(request.user)
#             is_followed = True
#         context = {
#             "is_followed": is_followed,
#             "followersCount": user.followers.all().count(),
#             "followingsCount": user.followings.all().count(),
#         }
#         return JsonResponse(context)
#     return redirect("accounts:profile", user.username)

@login_required
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필 정보가 성공적으로 변경되었습니다.")
            return redirect("accounts:profile", request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    messages.success(request, "탈퇴 완료")
    return redirect("main")