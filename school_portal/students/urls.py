from django.urls import path
from .views import register_student, student_list, edit_student, delete_student, student_detail, export_students_excel, login_view, logout_view

urlpatterns = [
    path('', register_student, name='register'),
    path('students/', student_list, name='students'),
    path('edit/<int:id>/', edit_student, name='edit'),
    path('delete/<int:id>/', delete_student, name='delete'),
    path('student/<int:id>/', student_detail, name='student_detail'),
    path('export/', export_students_excel, name='export_students'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
