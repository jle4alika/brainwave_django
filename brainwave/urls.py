"""
URL configuration for brainwave project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static  # Импортируем функцию для обработки статических файлов
from django.conf import settings  # Импортируем настройки проекта
from django.shortcuts import render, redirect
from django.urls import re_path
from django.views.static import serve
from lk.models import *
from lk.models import User_achivements, Achivement
from lk.views import UserRegisterView, UserLoginView, UserLogoutView, profile  # Импортируем представления из приложения lk
from categories.views import categories, course
from courses.views import lesson, tests

def index(request):
    return render(request, 'home.html', context={
        'image': request.user.image.url if request.user.is_authenticated else None,
    })

def achivements(request):
    if request.user.is_authenticated:
        user = User.objects.values(
            'registred_time',
        ).filter(username=request.user)
        user = user.get()

        not_passed = [obj for obj in Achivement.objects.all()]

        
        passed = User_achivements.objects.filter(username=request.user).get() if User_achivements.objects.filter(username=request.user).exists() else [{'title': 'Первопроходец', 'description': 'Зарегистрироваться и войти в аккаунт', 'exp': 100, 'image': '/media/achievements/shagi.jpg', 'passed_time': user['registred_time']}]
        passed = passed if request.user.is_authenticated else []
        
        if len(passed) == 0:
            not_passed.append({'title': 'Первопроходец', 'description': 'Зарегистрироваться и войти в аккаунт', 'exp': 100, 'image': '/media/achievements/shagi.jpg'})
        
        all_exp_bonus = sum([a['exp'] for a in passed])
        all_achievements_count = len(not_passed) + 1
        passed_achievements_count = len(passed)
        
        passed_achievements_percent = passed_achievements_count / all_achievements_count * 100
        
        return render(request, 'achievements.html', context={
            'image': request.user.image.url if request.user.is_authenticated else None,
            'passed': passed,
            'not_passed': not_passed,
            'passed_achievements_count': passed_achievements_count,
            'passed_achievements_percent': passed_achievements_percent,
            'all_achievements_count': all_achievements_count,
            'all_exp_bonus': all_exp_bonus
        })
    else:
        not_passed = [obj for obj in Achivement.objects.all()]
        not_passed.append({'title': 'Первопроходец', 'description': 'Зарегистрироваться и войти в аккаунт', 'exp': 100, 'image': '/media/achievements/shagi.jpg'})
        
        all_exp_bonus = 0
        all_achievements_count = len(not_passed)
        passed_achievements_count = 0
        passed_achievements_percent = 0
        
        return render(request, 'achievements.html', context={
            'image': request.user.image.url if request.user.is_authenticated else None,
            'passed': [],
            'not_passed': not_passed,
            'passed_achievements_count': passed_achievements_count,
            'passed_achievements_percent': passed_achievements_percent,
            'all_achievements_count': all_achievements_count,
            'all_exp_bonus': all_exp_bonus
        })

urlpatterns = [
    path('', index, name='home'),
    path('profile/', profile, name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('course/', course, name='course'),
    path('lesson/', lesson, name='lesson'),
    path('test/', tests, name='test'),
    path('categories/', categories, name='categories'),
    path('all-achievements/', achivements, name='all-achievements'),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^staticfiles/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Добавляем обработку статических файлов в режиме разработки
