from django.shortcuts import render
from django.views.decorators.http import require_safe

@require_safe
def base(request):
    return render(request, "base.html")