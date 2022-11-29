from django.shortcuts import render
from django.views.decorators.http import require_safe

@require_safe
def main(request):
    return render(request, "main.html")