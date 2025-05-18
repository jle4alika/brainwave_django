from django.db import models  # Импортируем базовый класс моделей Django
from django.contrib.auth.models import AbstractUser, UserManager  # Импортируем абстрактный класс пользователя и менеджер пользователей

import datetime  # Импортируем модуль datetime для работы с датами

# Создание пользовательской модели User
class User(AbstractUser, models.Model):
    """Модель пользователя, расширяющая стандартную модель AbstractUser."""

    __tablename__ = 'users'  # Указываем имя таблицы в базе данных

    # Поля модели
    
    username = models.CharField(max_length=255, unique=True)  # Уникальное имя пользователя
    
    full_name = models.CharField(max_length=255)  # Имя пользователя
    
    email = models.CharField(max_length=255)  # Электронная почта пользователя
    
    exp = models.BigIntegerField(default=100)  # EXP пользователя
    spended_time = models.BigIntegerField(default=0)  # Общее время обучения
    
    password = models.CharField(max_length=255)  # Пароль пользователя (не рекомендуется хранить в открытом виде)
    image = models.ImageField(upload_to='avatars/', default='avatar.png')  # Изображение профиля пользователя
    is_staff = models.BooleanField(default=False)  # Является ли пользователь сотрудником
    registred_time = models.DateField(default=datetime.datetime.now())
    
    USERNAME_FIELD = 'username'  # Обозначение поля юзернейма
    REQUIRED_FIELDS = []  # Обязательные поля при создании суперпользователя (оставлено пустым)
    PASSWORD_FIELD = 'password'  # Обозначение поля пароля

    objects = UserManager()  # Менеджер для работы с пользователями

    def __str__(self):
        """Возвращает строковое представление объекта User."""
        return self.username  # Возвращаем имя пользователя как строковое представление


class User_courses(models.Model):
    
    __tablename__ = 'users_courses'  # Указываем имя таблицы в базе данных
    
    # Поля модели
    
    username = models.CharField(max_length=255, default='')  # Уникальное имя пользователя
    
    lvls = models.IntegerField(default=1)  # Уровень 
    passed_lvls = models.IntegerField(default=0)   # Уровень 
    percent = models.IntegerField(default=0)

    difficulty = models.CharField(max_length=255, default='начальный')  # Уровень 
    title = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    full_description = models.CharField(max_length=255, default='')
    exp = models.BigIntegerField(default=0)  # EXP пользователя
    spended_time = models.BigIntegerField(default=0)  # Общее время обучения
    
    state = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username  # Возвращаем имя пользователя как строковое представление


class User_lvls(models.Model):
    
    __tablename__ = 'users_lvls'  # Указываем имя таблицы в базе данных
    
    # Поля модели

    username = models.CharField(max_length=255, default='')  # Уникальное имя пользователя
    
    course_title = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    theme = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    
    number = models.IntegerField(default=1)
    
    exp = models.BigIntegerField(default=0)  # EXP
    
    text = models.CharField(default='')
    spended_time = models.BigIntegerField(default=0)  # Общее время обучения
    
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.username  # Возвращаем имя пользователя как строковое представление

     
class User_tests(models.Model):
    
    __tablename__ = 'users_tests'  # Указываем имя таблицы в базе данных
    
    # Поля модели

    username = models.CharField(max_length=255, default='')  # Уникальное имя пользователя
    
    course_title = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    
    number = models.IntegerField(default=1)
    questions = models.CharField(max_length=255, default='')
    
    answer = models.CharField(max_length=255, default='')
    
    exp = models.BigIntegerField(default=0)  # EXP

    spended_time = models.BigIntegerField(default=0)  # Общее время обучения
    
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.username  # Возвращаем имя пользователя как строковое представление

class User_achivements(models.Model):

    __tablename__ = 'users_achivements'  # Указываем имя таблицы в базе данных
        
    # Поля модели
    username = models.CharField(max_length=255, default='')  # Уникальное имя пользователя
    
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='achievements/', default='avatar.png')
    exp = models.BigIntegerField(default=0)
    passed_time = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return self.username  # Возвращаем имя пользователя как строковое представление

class Achivement(models.Model):
    
    __tablename__ = 'achivements'  # Указываем имя таблицы в базе данных
    
    # Поля модели
    
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='achievements/', default='avatar.png')
    exp = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.title  # Возвращаем заголовок как строковое представление
