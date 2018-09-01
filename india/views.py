from django.shortcuts import render

# Create your views here.

def india(request):
    return render(request, 'hi.html')