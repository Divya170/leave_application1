from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    dob = models.DateField()
    password = models.CharField(max_length=128)  # Will store hashed passwords



class LeaveApplication(models.Model):
    STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    student_name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    department = models.CharField(max_length=50)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Requested')
    leave_days = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.status}"


   
