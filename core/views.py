from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Rooms, Leads, Period, Course, Groups, Teacher, Student
from django.contrib import messages
from .forms import LeadToStudentForm, GroupsForms, CourseForms, LeadsForms, LeadsUpdateForms, PeriodForms, TeacherForms, StudentForm
# Create your views here.


def home(request):

    return render(request, 'index.html', {})

# ------------leads create------------


def leads(request):
    form = LeadsForms()
    if request.method == 'POST':
        form = LeadsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('periods')
    context = {'form': form}
    return render(request, template_name='new_leads.html', context=context)


# def leads_list(request):
#     unarchived = Leads.objects.filter(archive=False)
#     new = unarchived.filter(ledstype='new')
#     inprogress = unarchived.filter(ledstype='inprogress')
#     colected = unarchived.filter(ledstype='colected')
#     n = new.count()
#     i = inprogress.count()
#     c = colected.count()
#     context = {'new': new,
#                'inprogress': inprogress,
#                'colected': colected,
#                "n": n,
#                "i": i,
#                "c": c
#                }

#     return render(request, 'card.html', context)


def lead_update(request, pk):
    lead = Leads.objects.get(id=pk)
    form = LeadsUpdateForms(instance=lead)
    print(form)
    if request.method == 'POST':
        form = LeadsUpdateForms(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('periods')
    leadupdate = True
    context = {'form': form,
               'leadupdate': leadupdate,
               'lead': lead,
               }
    return render(request, 'update.html', context)


def lead_delete(request, pk):
    lead = get_object_or_404(Leads, pk=pk)
    if lead:
        if request.method == 'POST':
            lead.archive = True
            lead.save()
            messages.success(request, 'Lead deleted successfully.')
            #context qilish kerak
            return redirect('periods')
        context = {'lead': lead}
        return render(request, 'delete.html', context)
    else:
        return redirect('periods')


# <------------- period (hodisalar)----------->

def period(request):
    periods = Period.objects.all()
    context = {
        'periods': periods,
    }
    return render(request, 'card2.html', context)


def period_add(request):
    form = PeriodForms()
    if request.method == 'POST':
        form = PeriodForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('periods')
    context = {'form': form}
    return render(request, 'add_period.html', context)


def period_update(request, pk):
    period = get_object_or_404(Period, pk)
    form = PeriodForms(instance=period)
    if request.method == 'POST':
        form = PeriodForms(request.POST, instance=period)
        if form.is_valid():
            form.save()
            return redirect('periods')
    context = {
        'form': form
    }

    return render(request, 'update.html', context)


def group(request):
    groups = Groups.objects.all()
    rooms = Rooms.objects.all()
    context = {
        'groups': groups,
        'rooms': rooms
    }
    return render(request, 'groups.html', context)


def add_group(request):
    group = Groups.objects.all()
    form = GroupsForms()
    if request.method == 'POST':
        form = GroupsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    context = {'form': form}
    return render(request, 'add_group.html', context)


def group_update(request, pk):
    group = get_object_or_404(Groups, pk=pk)
    form = GroupsForms(instance=group)
    if request.method == 'POST':
        form = GroupsForms(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups')
    context = {'form': form}
    return render(request, 'add_group.html', context)


def group_delete(request, pk):
    group = get_object_or_404(Groups, pk=pk)
    if request.method == 'POST':
        group.delete()
        messages.success(request, 'Group deleted successfully.')
        return redirect('groups')
    context = {'group': group}
    return render(request, 'delete.html', context)


def course(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)


def course_create(request):
    course = Course.objects.all()
    form = CourseForms(instance=course)
    if request.method == 'POST':
        form = CourseForms(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    context = {'form': form}
    return render(request, 'add_course.html', context)


def course_update(request, pk):
    group = get_object_or_404(Course, pk=pk)
    form = CourseForms(instance=group)
    if request.method == 'POST':
        form = CourseForms(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('courses')
    context = {'form': form}
    return render(request, 'add_course.html', context)


def course_delete(request, pk):
    group = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        group.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('courses')
    context = {'group': group}
    return render(request, 'delete.html', context)


# def group_filter_by_day(request, day):
#     today = Groups.objects.filter(day__name=day)
#     weekdays = Groups.objects.all()
#     year = Groups.objects.filter(day__name=day).values('beginday__year').distinct()
#     month = Groups.objects.filter(day__name=day).values('beginday__month').distinct()
#     context = {
#         'today':today,
#         'weekdays':weekdays,
#         'year':year,
#         'month':month,
#     }
#     return render(request, 'today.html', context)


def teacher(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teachers.html', context)


def techer_create(request, pk):
    teacher = get_object_or_404
    form = TeacherForms()
    if request.method == 'POST':
        form = TeacherForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    context = {
        'form': form
    }
    return render(request, 'add_course.html', context)


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForms(instance=teacher)
    if request.method == 'POST':
        form = TeacherForms(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def techer_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher deleted')
        redirect('teachers')
    context = {
        'teacher': teacher
    }
    return render(request, 'delete.html', context)


# -----------------students-------------------------

def student(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students.html', context)


def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    student_create = True
    context = {
        'form': form,
        'student_create': student_create
    }
    return render(request, 'add_group.html', context)


# def lead_to_student(request, pk):
#     lead = get_object_or_404(Leads, pk=pk)
#     form = StudentForm(instance=lead)
#     if request.method == 'POST':
#         form = StudentForm(request.POST,instance=lead)
#         form.save()
#         if form.is_valid():
#             print(request.POST)
#             form.save()
#             lead.delete()
#             return redirect('students')
#     context = {
#         'forma':form
#     }
#     return render(request, 'lead_to_student.html', context)

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return redirect('students')
    student_updatee = True
    context = {
        'form': form,
        'student_update': student_updatee,
        'student': student,
    }
    studentupdate = True
    return render(request, 'update.html', context)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted')
        return redirect('students')
    context = {
        'student': student
    }
    studentdelete = True
    return render(request, 'delete.html', context)


def lead_to_sudent(request, pk):
    lead = get_object_or_404(Leads, pk=pk)
    form = LeadToStudentForm(instance=lead)
    if request.method == 'POST':
        form = LeadToStudentForm(request.POST)
        if form.is_valid():
            form.save()
            lead.archive = True
            lead.save()
            print('succsess')
            print('succsess')
            return redirect('students')
    context = {
        'form': form,
        'lead': lead,
    }
    return render(request, 'alohida.html', context)


def xisobot(request):
    leads = Leads.objects.all().count()
    students = Student.objects.all().count()
    monthly_leads = Leads.objects.filter(created_at__month=5).count()
    context = {
        'leads': leads,
        'student': students,
        'monthly_leads': monthly_leads
    }
    return render(request, 'xisobot.html', context)
