from django.shortcuts import render

# Create your views here.

def Goodmorning(request):
    return render(request, 'Goodmorning.html')