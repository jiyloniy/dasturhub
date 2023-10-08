from django.contrib import admin
from .models import Leads, Course, Groups, Teacher, Finance,Period,WeekDay,Rooms,Student
# Register your models here.
@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ['name','phone']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','price']

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','phone']


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['name','forPeriod']



@admin.register(WeekDay)
class CourseClass(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Student)
class StudentClass(admin.ModelAdmin):
    list_display = ['name','phone']
    search_fields = ['phone','name']