from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_safe,
)
from .forms import CustomUserChangeForm, CheckPasswordForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from magazine.models import Magazine


@require_safe
def profile(request, username):
    # get_user_model 확인
    user = get_object_or_404(get_user_model(), username=username)
    following_users = user.follow.all()
    bookmarks = Magazine.objects.filter(bookmark_users__exact=user)
    print(bookmarks)
    context = {
        "user": user,
        "following_users": following_users,
        'bookmarks' : bookmarks,
    }
    return render(request, "accounts/profile.html", context)


@login_required
def follow(request, username):
    user = get_user_model().objects.get(username=username)

    if request.user not in user.followers.all():
        if user != request.user:
            user.followers.add(request.user)
            is_following = True
        else:
            return redirect("accounts:profile", user.username)
    else:
        user.followers.remove(request.user)
        is_following = False

    context = {
        "is_followed": is_following,
        "followersCnt": user.followers.all().count(),
        "followingsCnt": user.follow.all().count(),
    }
    return JsonResponse(context)


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
    if request.method == "POST":
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            auth_logout(request)
            messages.success(request, "회원 탈퇴가 완료되었습니다.")
            return redirect("main")
    else:
        password_form = CheckPasswordForm(request.user)
    context = {"password_form": password_form}
    return render(request, "accounts/check_delete.html", context)
