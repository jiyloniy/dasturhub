from django.urls import path

from .views import lead_to_sudent,student_delete,student_update,student_create,student,teacher,course_delete,group_delete,group_update, course_update, add_group,course_create,group,home, leads,lead_delete,leads_list,lead_update,period,period_add,course

urlpatterns = [
    # path('', home, name='home'),
    path('leads/', leads, name='leadregister'),
    path("students/", student, name="students"),
    path("student-create", student_create, name="studentcreate"),
    path("student-update/<int:pk>/", student_update, name="student_update"),
    path("student-delete/<int:pk>/", student_delete ,name="student_delete"),
    path('lead-to-student/<int:pk>/', lead_to_sudent, name='leadtostudent'),
    path("addcourse/", course_create, name="addcourse"),
    path("addgroup/", add_group, name="add_group"),
    path("courses/<int:pk>", course_update, name="course_update"),
    path("groups/", group, name="groups"),
    path("groups/<int:pk>", group_update, name="group_update"),
    path("teachers/", teacher, name="teachers"),
    path("add_period/", period_add, name="period_add"),
    path("courses/", course, name="courses"),
    path('leads-list/',leads_list,name='listleads'),
    path("", period, name="periods"),
    path('lead-update/<int:pk>/',lead_update,name='lead_update'),
    path('lead-delete/<int:pk>/',lead_delete,name='lead_delete'),
    path('course-delete/<int:pk>/',course_delete,name='course_delete'),
    path('group-delete/<int:pk>/',group_delete,name='group_delete'),
]