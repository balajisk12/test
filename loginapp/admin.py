from django.contrib import admin
from .models import User,FacultyDetails,StudentDetails,LabDetails



admin.site.register(User)
admin.site.register(FacultyDetails)
admin.site.register(StudentDetails)
admin.site.register(LabDetails)

