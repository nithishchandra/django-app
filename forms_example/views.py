from django.shortcuts import render
from forms_example.forms import EmployeeForm

# Create your views here.

def empform(request):

    form = EmployeeForm()

    if request.method == 'POST':
        #print(request.method)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            pass

    return render(request, 'pro.html', {'form':form})

