from django.shortcuts import render

# Create your views here.
def eventhome(request):

    return render(request,'articles/eventhome.html')