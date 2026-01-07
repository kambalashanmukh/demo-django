from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Example@gmail.com'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'student_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5A'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 10'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 23'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Plot no:/Street'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Hyderabad'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Telangana'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 500081'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'parent_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234567890'}),
        }
