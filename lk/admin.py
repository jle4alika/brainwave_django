from django.contrib import admin

# Register your models here.

from .models import User, User_tests, User_courses, User_achivements, Achivement

admin.site.register(User)
admin.site.register(User_courses)
admin.site.register(User_tests)
admin.site.register(User_achivements)
admin.site.register(Achivement)