from django.db import models

# Create your models here.

class Course(models.Model):
    
    __tablename__ = 'courses'  # Указываем имя таблицы в базе данных
    
    # Поля модели
    
    image = models.ImageField(upload_to='courses/', default='')
    
    title = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    
    difficulty = models.CharField(max_length=255, default='начальный')
    exp = models.BigIntegerField(default=0)  # EXP
    lessons_count = models.IntegerField(default=1)
    tests_count = models.IntegerField(default=1)
    spended_time = models.BigIntegerField(default=0)  # Общее время обучения
    
    description = models.CharField(max_length=255, default='') # Описание курса
    full_description = models.CharField(max_length=255, default='') # Описание курса
    
    def __str__(self):
        """Возвращает строковое представление объекта Course."""
        return self.title  # Возвращаем название категории


class Course_lvl(models.Model):
    
    __tablename__ = 'courses_lvls'  # Указываем имя таблицы в базе данных
    
    # Поля модели
    course_title = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    theme = models.CharField(max_length=255, default='')
    
    number = models.IntegerField(default=1)
    
    exp = models.BigIntegerField(default=0)  # EXP
    spended_time = models.BigIntegerField(default=0)  # Общее время обучения
    
    text = models.TextField(default='')
    
    def __str__(self):
        """Возвращает строковое представление объекта Course."""
        return self.title  # Возвращаем название категории


class Course_test(models.Model):
    
    __tablename__ = 'courses_tests'  # Указываем имя таблицы в базе данных
    
    # Поля модели
    course_title = models.CharField(max_length=255, default='')
    lesson_title = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    
    number = models.IntegerField(default=1)
    questions = models.CharField(max_length=255, default='')
    
    variant1 = models.CharField(max_length=255, default='')
    variant2 = models.CharField(max_length=255, default='')
    variant3 = models.CharField(max_length=255, default='')
    right_variant = models.CharField(max_length=255, default='')
    
    exp = models.BigIntegerField(default=0)  # EXP
    spended_time = models.BigIntegerField(default=0)  # Общее время обучения
    
    def __str__(self):
        """Возвращает строковое представление объекта Course."""
        return self.title  # Возвращаем название категории
