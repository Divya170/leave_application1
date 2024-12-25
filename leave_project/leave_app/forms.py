from django import forms
from django.contrib.auth.hashers import make_password
from leave_app.models import Student
from .models import LeaveApplication

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'department', 'year', 'gender', 'mobile', 'email', 'dob', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Render password field as a password input
        }

    def save(self, commit=True):
        student = super().save(commit=False)
        student.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            student.save()
        return student


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())






class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ['student_name', 'year', 'department', 'reason', 'leave_days']
