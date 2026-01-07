from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from openpyxl import Workbook
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def register_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'register.html', {'form': form})

@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

@login_required(login_url='login')
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('students')

    return render(request, 'edit.html', {'form': form})

@login_required(login_url='login')
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('students')

@login_required(login_url='login')
def student_list(request):
    search_query = request.GET.get('search', '')
    
    students = Student.objects.filter(
        Q(name__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(student_class__icontains=search_query)|
        Q(rollno__icontains=search_query)
    )

    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })

@login_required(login_url='login')
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {'student': student})

@login_required(login_url='login')
def export_students_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Students"

    # Header row
    ws.append(["Name", "Email", "DOB", "Gender", "Class", "Age", "Roll No", "Address", "City", "State", "Pincode", "Parent Name", "Parent Phone"])

    # Data rows
    for s in Student.objects.all():
        ws.append([s.name, s.email, s.dob, s.gender, s.student_class, s.age, s.rollno, s.address, s.city, s.state, s.pincode, s.parent_name, s.parent_phone])

    # Response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=students.xlsx"

    wb.save(response)
    return response

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
