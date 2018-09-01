from django.shortcuts import render

from chennai.forms import formExample

# Create your views here.

def chennai(request):
    form = formExample()
    print(form)
    d1 = {
        'form':form
        #'name':'Nithish',
        #'email':'nithish@yahoo.com',
        #'l1':[1,2,3,4],
        #'d1':{'city':'Bangalore', 'address':'BTM' }
    }
    return render(
        request,
        'graduation.html',
        d1
    )