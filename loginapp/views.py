# views.py
from django.shortcuts import render, redirect
from .models import User

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()

        if user:
            if user.is_faculty:
                return redirect('faculty_portal')
            elif user.is_student:
                return redirect('student_portal')
        else:
            error_message = "Invalid username or password."
    
    return render(request, 'login.html', {'error_message': error_message})


def faculty_portal(request):
    return render(request, 'faculty_portal.html')

def student_portal(request):
    return render(request, 'student_portal.html')



# Student portal sub-files(update code dynamically on rigth side container)

def student_profile(request):
    return render(request, 'student/student_profile.html')

def student_available_slots(request):
    return render(request, 'student/student_availableslots.html')

def student_book_slot(request):
    return render(request, 'student/student_bookslot.html')

def student_wild_card(request):
    return render(request, 'student/student_wildcard.html')

def student_special_cases(request):
    return render(request, 'student/student_specialcases.html')

def student_result(request):
    return render(request, 'student/student_result.html')

def student_lab_change(request):
    return render(request, 'student/student_labchange.html')

def student_lab_details(request):
    return render(request, 'student/student_labdetails.html')


# Faculty portal sub-files(update code dynamically on rigth side container)

def faculty_profile(request):
    return render(request, 'faculty/faculty_profile.html')

def faculty_lab_admission(request):
    return render(request, 'faculty/faculty_labadmission.html')

def faculty_change_lab(request):
    return render(request, 'faculty/faculty_changelab.html')

def faculty_lab_details(request):
    return render(request, 'faculty/faculty_labdetails.html')
