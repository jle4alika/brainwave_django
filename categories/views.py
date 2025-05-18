from django.shortcuts import render, redirect
from .models import Course, Course_lvl, Course_test
from lk.models import User_courses
# Create your views here.

def categories(request):
    categories_list = Course.objects.values(
        'title',
        'category',
        'image',
        'description',
        'exp'
    ).all()
    categories_buttons = set([a['category'] for a in categories_list])
    
    return render(request, 'categories.html', context={
        'categories': categories_list,
        'categories_buttons': categories_buttons
    })
    
def course(request):
    title = request.GET.get('title', 'Заголовок не передан')

    course = Course.objects.values(
        'title',
        'category',
        'difficulty',
        'exp',
        'lessons_count',
        'tests_count',
        'spended_time',
        'description',
        'full_description',
        'image'
        ).filter(title=title).get()
    
    course_lvls = [obj for obj in Course_lvl.objects.values(
        'title',
        'category',
        'theme',
        'exp',
        'number',
        'spended_time',
        'text'
        ).filter(course_title=title).all()]
    
    course_tests = [obj for obj in Course_test.objects.values(
        'title',
        'category',
        'exp',
        'number',
        'spended_time',
        'questions',
        'variant1',
        'variant2',
        'variant3',
        'right_variant'
        ).filter(course_title=title).all()] if Course_test.objects.filter(course_title=title).exists() else []
    
    User_courses.objects.get_or_create(
        title=course['title'],
        username=request.user,
        category=course['category'],
        difficulty=course['difficulty'],
        exp=course['exp'],
        lvls=course['lessons_count'],
        spended_time=course['spended_time'],
        description=course['description'],
        full_description=course['full_description']
    )
    
    user = [obj for obj in User_courses.objects.values(
        'passed_lvls',
        'lvls'
    ).filter(username=request.user, title=course['title']).all()]
    
    print(course_lvls)
    print(len(course_lvls))
    
    return render(request, 'course.html',
                  context={
                      'course': course,
                      'percent':[ user['passed_lvls'] / user['lvls'] * 100 for user in user],
                      'course_lvls': course_lvls,
                      'course_title': title,
                      'lessons_count': len(course_lvls),
                      'tests_count': len(course_tests),
                      'title': title
                  })