
from django.shortcuts import render, redirect,HttpResponse
from leave_app.forms import StudentForm,LoginForm
from leave_app.models import Student
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import LeaveApplication
from .forms import LeaveApplicationForm


# Create your views here.

def sregister(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('slogin')
    else:
        form = StudentForm()
    
    return render(request, 'index.html', {'form': form})


def slogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(name=name)
                if check_password(password, student.password):
                    request.session['student_id'] = student.id
                    return render(request,'home.html')
                else:
                    return HttpResponse('Error: Invalid credentials', status=401)
            except Student.DoesNotExist:
                return HttpResponse('Error: Invalid credentials', status=401)
    else:
        form = LoginForm()
    
    return render(request, 'slogin.html', {'form': form})



def user_logout(request):
    logout(request)  # Clears the session
    return redirect('slogin')  # Redirect to login page



@login_required(login_url='slogin')  # Redirects to login if the user is not authenticated
def home(request):
    return render(request, 'home.html')  # Render the home page template


def dashboard(request):
    if request.method == "POST":
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with your URL name
    else:
        form = LeaveApplicationForm()

    leave_applications = LeaveApplication.objects.all()
    return render(request, 'dashboard.html', {'form': form, 'leave_applications': leave_applications})

def student_status(request):
    student_name = request.GET.get('student_name')
    leave_status = LeaveApplication.objects.filter(student_name=student_name)
    return render(request, 'status.html', {'leave_status': leave_status, 'student_name': student_name})
