from django.shortcuts import render
from categories.models import Course_lvl, Course_test
from lk.models import User_lvls, User_tests, User, User_courses
# Create your views here.


def lesson(request):
    course_title = request.GET.get('course_title', 'Заголовок не передан')
    title = request.GET.get('title', 'Заголовок не передан')
    number = int(request.GET.get('number', 0))
    
    lesson = Course_lvl.objects.values(
        'course_title',
        'number',
        'title',
        'text',
        'theme',
        'spended_time',
        'category',
        'exp'
    ).filter(course_title=course_title, number=number).get()
    
    next_lesson = Course_lvl.objects.values(
        'course_title',
        'number',
        'title',
        'text',
    ).filter(course_title=course_title, number=number+1).get() if Course_lvl.objects.filter(course_title=course_title, number=number+1).exists() else None
    
    test = Course_test.objects.values(
        'title'
    ).filter(course_title=course_title, number=number).get if Course_test.objects.filter(course_title=course_title, number=number).exists() else None

    User_lvls.objects.get_or_create(
        username=request.user,
        title=title,
        course_title=course_title,
        category=lesson['category'],
        exp=lesson['exp'],
        number=lesson['number'],
        spended_time=lesson['spended_time'],
        text=lesson['text'],
        theme=lesson['theme']
    )
    
    return render(request, 'lesson.html', context={
        'lesson': lesson,
        'next_lesson': next_lesson,
        'test': test
    })
    
def tests(request):
    if request.method == 'POST':
        course_title = request.GET.get('course_title', 'Заголовок не передан')
        title = request.GET.get('title', 'Заголовок не передан')
        number = int(request.GET.get('number', 0))
        
        test = Course_test.objects.values(
            'title',
            'course_title',
            'lesson_title',
            'questions',
            'variant1',
            'variant2',
            'variant3',
            'right_variant'
        ).filter(course_title=course_title, lesson_title=title, number=number).get() if Course_test.objects.filter(course_title=course_title, lesson_title=title, number=number).exists() else None
        answers = []
        right_answers = []
        
        for number in range(1, len(test['questions'].split(','))+1):
            answers.append(int(request.POST.get(f'q{number}'))) if int(request.POST.get(f'q{number}')) == 0 \
            else right_answers.append(int(request.POST.get(f'q{number}')))
        
        percent = round(len(right_answers) / (len(answers) + len(right_answers)) * 100, 2)
        exp = len(right_answers) * 15 if len(right_answers) >= 1 else 1 * 15
        passed = True if percent >= 70 else False
        div_class = 'result-pass' if passed else 'result-fail'
        total = 'Тест пройден! Отличная работа.' if passed else 'Тест не пройден. Попробуйте еще раз.'
        
        user = User.objects.get(username=request.user)
        
        user.exp += exp
        user.save()

        lvls = User_courses.objects.values('lvls').filter(username=request.user).get()['lvls']
        user_course = User_courses.objects.get(username=request.user)

        user_course.passed_lvls += 1 if passed else 0
        user_course.save()
        
        user_course = User_courses.objects.get(username=request.user)
        passed_lvls = User_courses.objects.values('passed_lvls').filter(username=request.user).get()['passed_lvls']
        if passed_lvls == lvls:
            user = User_courses.objects.get(username=request.user)
            user.state = True
            user.save()
        
        user_course.percent = passed_lvls / lvls * 100
        
        user_course.save()
        
        lesson = Course_lvl.objects.values(
            'course_title',
            'number',
            'title',
            'text',
            'theme',
            'spended_time',
            'category',
            'exp'
            ).filter(course_title=course_title, number=number).get()
        
        next_lesson = Course_lvl.objects.values(
            'course_title',
            'number',
            'title',
            'text',
            ).filter(course_title=course_title, number=number+1).get() if Course_lvl.objects.filter(course_title=course_title, number=number+1).exists() else None
        
        
        return render(request, 'result.html', context={
            'percent': percent,
            'passed': passed,
            'exp': exp,
            'total': total,
            'div_class': div_class,
            'next_lesson' : next_lesson,
            'lesson': lesson
        })
    
    course_title = request.GET.get('course_title', 'Заголовок не передан')
    title = request.GET.get('title', 'Заголовок не передан')
    number = int(request.GET.get('number', 0))
    questions = []
    
    test = Course_test.objects.values(
        'title',
        'course_title',
        'lesson_title',
        'questions',
        'variant1',
        'variant2',
        'variant3',
        'right_variant',
        'spended_time',
        'exp',
        'number',
        'category'
    ).filter(course_title=course_title, lesson_title=title, number=number).get() if Course_test.objects.filter(course_title=course_title, lesson_title=title, number=number).exists() else None
    
    User_tests.objects.get_or_create(
        username=request.user,
        category=test['category'],
        exp=test['exp'],
        spended_time=test['spended_time'],
        course_title=test['course_title'],
        title=test['title'],
        number=test['number'],
        questions=test['questions'],
    )
    
    for number, question, variant1, variant2, variant3, right_variant in zip(
        [
            num for num in range(1, 1 + len(
            test['questions'].split(',')))
            ],
        test['questions'].split(','),
        test['variant1'].split(','),
        test['variant2'].split(','),
        test['variant3'].split(','),
        test['right_variant'].split(',')
        ):
        
        question = {
            'number': number,
            'text': question,
            'variant1': {'value': 0, 'text': variant1},
            'variant2': {'value': 1, 'text': right_variant},
            'variant3': {'value': 0, 'text': variant2},
            'variant4': {'value': 0, 'text': variant3},
        }
        
        questions.append(question)
    
    return render(request, 'test.html', context={
        'test': test,
        'questions': questions
    })
    