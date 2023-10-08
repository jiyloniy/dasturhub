from django import forms
from .models import Groups, Course, Leads, Period, Teacher,Student  # Leads modelini import qilib oling

class LeadsForms(forms.ModelForm):
    class Meta:
        model = Leads  # Shu yerdagi modelni ko'rsatish
        fields = '__all__'  # Barcha maydonlarni foydalanish

class LeadsUpdateForms(forms.ModelForm):
    class Meta:
        model = Leads  # Shu yerdagi modelni ko'rsatish
        fields = '__all__'

class LeadsDeleteForms(forms.ModelForm):
    class Meta:
        model = Leads  # Shu yerdagi modelni ko'rsatish
        fields = '__all__'

class PeriodForms(forms.ModelForm):
    class Meta:
        model = Period
        fields = '__all__'

class GroupsForms(forms.ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'

class CourseForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class TeacherForms(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'

class LeadToStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'