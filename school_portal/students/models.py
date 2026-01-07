from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # Student
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    student_class = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    rollno = models.CharField(max_length=20, null=True, blank=True)

    # Address
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    # Parent
    parent_name = models.CharField(max_length=100, null=True, blank=True)
    parent_phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name
