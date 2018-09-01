from django.shortcuts import render

# Create your views here.


def helloDjango(request):
    return render(request, 'hello.html')

def hellonithish(request):
    #print(request.method)
    #print(request.GET)
    print(request.GET['name'])
    print(request.GET['email'])
    return render(request, 'hello nithish.html')
