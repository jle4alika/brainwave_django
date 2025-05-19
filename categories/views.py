from django.shortcuts import render, redirect
from .models import Course, Course_lvl, Course_test
from lk.models import User_courses, User_lvls
# Create your views here.

def categories(request):
    if request.user.is_authenticated:
        categories_list = Course.objects.values(
            'title',
            'category',
            'image',
            'description',
            'exp',
            'lessons_count'
        ).all()
        categories_buttons = set([a['category'] for a in categories_list])
        
        for category in categories_list:
            category['user_course'] = User_courses.objects.filter(title=category['title'], username=request.user).exists()
            
        return render(request, 'categories.html', context={
            'image': request.user.image.url if request.user.is_authenticated else None,
            'categories': categories_list,
            'categories_buttons': categories_buttons
        })
        
    else:
        categories_list = Course.objects.values(
            'title',
            'category',
            'image',
            'description',
            'exp',
            'lessons_count'
        ).all()
        categories_buttons = set([a['category'] for a in categories_list])

        return render(request, 'categories.html', context={
            'image': request.user.image.url if request.user.is_authenticated else None,
            'categories': categories_list,
            'categories_buttons': categories_buttons
        })
    
def course(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST.get('title')
            print(title)
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
            return redirect(f'/course/?title={title}')
        else:
            return redirect('/register/')
        
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
    
    user = User_courses.objects.values(
        'passed_lvls',
        'lvls'
    ).filter(username=request.user, title=course['title']).get() if User_courses.objects.filter(username=request.user, title=course['title']).exists() and request.user.is_authenticated else None
    
    print(user)

    if request.user.is_authenticated:
        for lesson in course_lvls:
            lesson['passed'] = True if User_lvls.objects.filter(course_title=course['title'], username=request.user, title=lesson['title']).exists() else False
            print(lesson['passed'])
    
    
    return render(request, 'course.html',
                  context={
                      'image': request.user.image.url if request.user.is_authenticated else None,
                      'course': course,
                      'percent': round(user['passed_lvls'] / user['lvls'] * 100) if user else 0,
                      'course_lvls': course_lvls,
                      'course_title': title,
                      'lessons_count': len(course_lvls),
                      'tests_count': len(course_tests),
                      'title': title,
                      'user_course': True if user else False
                  })
    
    
def error_404_view(request):
    return render(request, '404.html')