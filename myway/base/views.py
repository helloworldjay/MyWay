from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import os
import math
import requests
# Create your views here.
def get_home(request):
    return render(request, 'base/index.html', {})

def get_contact(request):
    return render(request, 'base/contact.html', {})

def fhp_explain(request):
    return render(request, 'base/fhp_explain.html', {})

def sign_up(request):
    context= {}

    # POST Method
    if request.method == 'POST':
        if (request.POST['username'] and request.POST['password'] and request.POST['password_check']):
            if (request.POST['password'] == request.POST['password_check']):
                new_user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                )

                auth.login(request, new_user)
                return redirect('get_home')
            else:
                context['error'] = '비 밀 번 호 를  다 시  확 인 해 주 세 요.'
        else:
            context['error'] = '아 이 디 와  비 밀 번 호 를  다 시  확 인 해 주 세 요 .'
    # GET Method
    return render(request, 'base/sign_up.html', context)

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
                return redirect('get_home')
            else:
                context['error'] = '아 이 디 와  비 밀 번 호 를  다 시  확 인 해 주 세 요 .'
        else:
            context['error'] = '아 이 디 와  비 밀 번 호 를  다 시  확 인 해 주 세 요 .'
    
    # GET Method
    return render(request, 'base/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('posts:index')

def fhp_check(request):
    return render(request,'base/fhp_check.html',{})

def fhp_check_check(request, user_photo):
    print(os.path)
    file_name = None
    if request.FILES:
        file_name = request.FILES['check_photo']
    APP_KEY = '8676c07b42dd5a954ad0d0d2a1d3025c'
    IMAGE_FILE_PATH = None
    if user_photo != 'None':
        IMAGE_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),user_photo)
    else:
        try:
            IMAGE_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),file_name)
            print(IMAGE_FILE_PATH,'sibal')
        except:
            return render(request, 'base/fhp_check.html',{'result': '사진 인식에 실패하였습니다.'})
    # print(IMAGE_FILE_PATH)
    IMAGE_FILE_PATH = request.FILES
    # print(request.FILES['check'])
    session = requests.Session()
    session.headers.update({'Authorization': 'KakaoAK ' + APP_KEY})
    # 파일로 이미지 입력시
    with open(IMAGE_FILE_PATH, 'rb') as f:
        response = session.post('https://cv-api.kakaobrain.com/pose', files=[('file', f)])
    json_data=response.json()[0]['keypoints']
    #기준값
    for_neck_check=round(math.atan(40*(math.pi/180)),6)
    #  귀 x         어깨 x
    x=json_data[12]-json_data[18]
    #  귀 y          어깨 y
    y=json_data[13]-json_data[19]
    res = round(y/x,6)
        #측정값  기준값
    if res<=for_neck_check:
        result ="거북목이 맞습니다."
    else:
        result ="거북목이 아닙니다."
    context={
        'result':result
    }
    return render(request,'base/fhp_check.html',context)