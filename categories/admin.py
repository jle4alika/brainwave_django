from django.contrib import admin

# Register your models here.

from .models import Course, Course_lvl, Course_test

admin.site.register(Course)
admin.site.register(Course_lvl)
admin.site.register(Course_test)