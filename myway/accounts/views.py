from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def sign_up(request):
    context= {}

    # POST Method
    if request.mehotd == 'POST':
        if (request.POST['username'] and request.POST['password'] and request.POST['password_check']):
            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            auth.login(request, new_user)
            return redirect('posts:index')
        else:
            context['error'] = '아 이 디 와  비 밀 번 호 를  다 시  확 인 해 주 세 요 .'
    # GET Method
    return render(request, 'accounts/sign_up.html', context)

def login(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:

            user = auth.authenticate(
                request,
                username= request.POST['username'],
                password= request.POST['password']
            )

            if user is not None:
                auth.login(request, user)
                return redirect('post:index')
            else:
                context['error'] = '아 이 디 와  비 밀 번 호 를  다 시  확 인 해 주 세 요 .'
        else:
            context['error'] = '아 이 디 와  비 밀 번 호 를  다 시  확 인 해 주 세 요 .'
    
    # GET Method
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('posts:index')