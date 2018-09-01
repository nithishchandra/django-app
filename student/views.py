from django.shortcuts import render, redirect, HttpResponse
from student.forms import StudentForm
from student.models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.
def create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'stu/create.html', {'form':form})

@login_required(login_url='/sites/signin')

def index(request):

    #return HttpResponse("<h4>410 gone</h4>")
    data = Student.objects.all()
    return render(request, 'stu/index.html', {'data':data})
    pass

def update(request, pk):
    data = Student.objects.get(id=pk)
    form = StudentForm(instance=data)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'stu/update.html', {'form': form})


def delete(request, pk):
    data = Student.objects.get(id=pk)
    data.delete()
    return redirect(index)

def view(reuqest, pk):
    data = Student.objects.get(id=pk)
    #select * from student where id=pk
    return render(reuqest, 'stu/view.html', {'data':data})