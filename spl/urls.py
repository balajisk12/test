"""
URL configuration for spl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from loginapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('faculty/', views.faculty_portal, name='faculty_portal'),
    path('student/', views.student_portal, name='student_portal'),

    path('student_profile/', views.student_profile, name='student_profile'),
    path('student_availableslots/', views.student_available_slots, name='student_available_slots'),
    path('student_bookslot/', views.student_book_slot, name='student_book_slot'),
    path('student_wildcard/', views.student_wild_card, name='student_wild_card'),
    path('student_specialcases/', views.student_special_cases, name='student_special_cases'),
    path('student_result/', views.student_result, name='student_result'),
    path('student_labchange/', views.student_lab_change, name='student_lab_change'),
    path('student_labdetails/', views.student_lab_details, name='student_lab_details'),

    path('faculty_profile/', views.faculty_profile, name='faculty_profile'),
    path('faculty_labadmission/', views.faculty_lab_admission, name='faculty_lab_admission'),
    path('faculty_changelab/', views.faculty_change_lab, name='faculty_change_lab'),
    path('faculty_labdetails/', views.faculty_lab_details, name='faculty_lab_details'),


]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #to upload image in xampp(MySql)








