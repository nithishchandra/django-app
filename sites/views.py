from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sites.forms import LoginForm
# Create your views here.
def UserSignin(request):

    if request.user.username:
        return redirect(Home)
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data['username']
            password =form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is None:
                message = 'Invalid user!'
            else:
                login(request, user)
                request.session['email'] = 'nithish@gmail.com'
                request.session['phone'] = 9840344385
                request.session['city'] = 'bangalore'
                #del request.session['city']
                return redirect(Home)

    return render(
        request,
        'user_auth/signin.html',
        {
            'form':form, 'msg' : message
        }
    )

def Home(request):
    return render(request, 'user_auth/home.html')

def UserLogout(request):
    if 'city' in request.session:
        del request.session['city']
    logout(request)
    return redirect(UserSignin)

def UserSignup(request):

    if request.user.username:
        return redirect(Home)
    form = UserCreationForm()
    message = ''
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = User()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user.username = username
            user.set_password(password)
            user.save()
            message = 'Registration done successfully'

    return render(
        request,
        'user_auth/signup.html',
        {'form':form, 'msg':message}
    )