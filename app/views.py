from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from .functions import *
from .models import *


def home(request):
    return render(request, 'app/home.html')


def login(request):
    if request.user.is_authenticated:
        objs = Dssat_cp.objects.all().filter(user=request.user)
        if objs.first():
            empty = 'NO'
        else:
            empty = 'YES'

        context = {
            'user': request.user,
            'objs': objs,
            'empty': empty,
        }
        return render(request, 'app/profile.html', context=context)
    else:
        return render(request, 'app/login.html')


def signup(request):
    email = request.POST['email']
    password = request.POST['password']
    obj = User.objects.all().filter(username=email).first()
    if obj:
        context = {
            'type' : 'signup',
            'color': 'red',
            'msg' : 'This email already exists',
        }
        return render(request, 'app/login.html', context=context)
    else:
        user = User.objects.create_user(username=email, password=password)
        context = {
            'type' : 'signup',
            'color': 'green',
            'msg' : 'Your account has been successfully created',
        }
        return render(request, 'app/login.html', context=context)


def signin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        dj_login(request, user)
        objs = Dssat_cp.objects.all().filter(user=request.user)
        if objs.first():
            empty = 'NO'
        else:
            empty = 'YES'

        context = {
            'user': request.user,
            'objs': objs,
            'empty': empty,
        }
        return render(request, 'app/profile.html', context=context)
    else:
        context = {
            'type' : 'signin',
            'msg' : 'Username or Password is wrong',
        }
        return render(request, 'app/login.html', context=context)


def computing(request):
    if request.user.is_authenticated:
        return render(request, 'app/computing.html')
    else:
        context = {
            'type' : 'signin',
            'msg' : 'First login to your account',
        }
        return render(request, 'app/login.html', context=context)

def compute(request):
    plant = request.POST['plant']
    soil = request.POST['soil']
    tmax = request.POST['tmax']
    tmin = request.POST['tmin']
    rain = request.POST['rain']
    srad = request.POST['srad']
    rhum = request.POST['rhum']
    plant_date = request.POST['plant_date']
    harvest_date = request.POST['harvest_date']

    inp = {
        'plant': plant,
        'soil': soil,
        'tmax': float(tmax),
        'tmin': float(tmin),
        'rain': float(rain),
        'srad': float(srad),
        'rhum': float(rhum),
        'plant_date': plant_date,
        'harvest_date': harvest_date,
    }

    oup = dssat_computing(inp)

    context = inp.copy()
    for key, value in oup.items():
        context[key] = value

    obj = Dssat_cp(
        user=request.user,
        tmax = context['tmax'],
        tmin = context['tmin'],
        rain = context['rain'],
        srad = context['srad'],
        rhum = context['rhum'],
        date = context['plant_date'],
        hdate = context['harvest_date'],
        plant = context['plant'],
        soil = context['soil'],
        DAP = context['DAP'],
        LAID = context['LAID'],
        GSTD = context['GSTD'],
        SWAD = context['SWAD'],
        LWAD = context['LWAD'],
        GWAD = context['GWAD'],
        GAD = context['GAD'],
        GWGD = context['GWGD'],
        HIAD = context['HIAD'],
        CWAD = context['CWAD'],
        )
    obj.save()

    return render(request, 'app/computing.html', context=context)


def logout(request):
    dj_logout(request)
    return render(request, 'app/home.html')
