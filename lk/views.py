from django.shortcuts import render

import sys  # Импортируем модуль sys

from django.http import HttpResponseRedirect  # Импортируем класс для перенаправления HTTP
from django.shortcuts import render, redirect  # Импортируем функции для рендеринга и перенаправления
from django.contrib.auth import logout  # Импортируем функцию выхода из системы
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage  # Импортируем класс для работы с файловой системой
from django.contrib.auth.models import User  # Импортируем модель пользователя
from django.views.generic import View  # Импортируем базовый класс представления

from .models import User, User_courses, User_tests, User_achivements, User_lvls  # Импортируем пользовательскую модель User из текущего приложения

from django.views.generic import CreateView  # Импортируем класс для создания представлений
from django.urls import reverse_lazy  # Импортируем функцию для обратного разрешения URL

from .forms import UserRegisterForm  # Импортируем форму регистрации пользователя
from .forms import UserLoginForm  # Импортируем форму входа пользователя
from .forms import UserInfoChangeForm
from django.contrib.messages.views import SuccessMessageMixin  # Импортируем класс для отображения сообщений об успехе
from django.contrib.auth.views import LoginView  # Импортируем класс представления входа


def profile(request):
    """Представление личного кабинета пользователя."""
    if request.user.is_authenticated:  # Проверяем, авторизован ли пользователь
        if request.method == 'POST':  # Проверяем метод запроса
            form = UserInfoChangeForm(request.POST, request.FILES, instance=request.user)
            
            if form.is_valid():
                form.save()
            return redirect('/profile/')
        else:
            form = UserInfoChangeForm(instance=request.user)
            # Получаем информацию о пользователе, который в данный момент вошел в систему
            user = User.objects.values(
                'username', 
                'full_name',
                'email',
                'is_staff',
                'exp',
                'spended_time',
                'registred_time',
            ).filter(username=request.user)
            
            
            user_courses_bool = User_courses.objects.values(
                'title',
                'exp',
                'lvls',
                'passed_lvls',
                'difficulty',
            ).filter(username=request.user).exists()
            if user_courses_bool:
                user_courses = [obj for obj in User_courses.objects.values(
                    'title',
                    'exp',
                    'lvls',
                    'passed_lvls',
                    'difficulty',
                    'percent'
                ).filter(username=request.user).all()]
                
                count_user_courses = len([obj for obj in User_courses.objects.values(
                    'title',
                    'exp',
                    'lvls',
                    'passed_lvls',
                    'difficulty',
                    'percent'
                ).filter(username=request.user, state=True).all()])
            else:
                count_user_courses = 0
            
            
            
            achivements_bool = User_achivements.objects.values(
                'title',
                'description',
            ).filter(username=request.user).exists()
            if achivements_bool:
                achivements = [obj for obj in User_achivements.objects.values(
                'title',
                'description',
                ).filter(username=request.user).all()]
                
                achivements_count = len(achivements)
            else:
                achivements_count = 0
            
            user_lvls_bool = User_lvls.objects.values(
                'title',
                'exp',
                'description',
                'spended_time'
            ).filter(username=request.user).exists()
            if user_lvls_bool:
                user_lvls = [obj for obj in User_lvls.objects.values(
                    'title',
                    'exp',
                    'description',
                    'spended_time',
                ).filter(username=request.user).all()]
                            
                passed_lessons_count = len(user_lvls)
            else:
                passed_lessons_count = 0
                
            user = user.get()

            user['lvl'] = (user['exp'] // 1000 + 1) if user['exp'] >= 1000 else 1
            user['exp'] = user['exp'] - (user['exp'] // 1000) * 1000 if user['exp'] >= 1000 else user['exp']
            return render(
                request,
                'profile.html',
                context={'user': user,
                         'image': request.user.image.url,
                         'courses_count': count_user_courses,
                         'achivements': achivements if achivements_bool else False,
                         'user_lvls': user_lvls if user_lvls_bool else False,
                         'user_courses': user_courses if user_courses_bool else False,
                         'achivements_count': achivements_count+1,
                         'passed_lessons_count': passed_lessons_count,
                         'lvl_percent': int(user['exp'] / 1000 * 100),
                         'form': form}
            )
    else:
        # Если пользователь не авторизован, перенаправляем его на страницу входа
        return redirect('/login/')

class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация | Brainwave'
        print(context)
        return context

class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'login.html'
    next_page = '/profile/'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход | Brainwave'
        return context
    


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


