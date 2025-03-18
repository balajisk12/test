from django.db import models

# User model
class User(models.Model):
    id = models.CharField(max_length=15, primary_key=True)  
    username = models.CharField(max_length=50, unique=True)  # Ensure usernames are unique
    password = models.CharField(max_length=128)  # Use a longer field for hashed passwords
    email = models.EmailField(unique=True)  # Ensure emails are unique
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    class Meta:
        db_table = 'Users'


# LabDetails model
class LabDetails(models.Model):
    lab_id = models.CharField(max_length=10, primary_key=True)
    lab_name = models.CharField(max_length=100)  
    faculty_in_charge = models.CharField(max_length=100)  
    faculty_incharge_id = models.CharField(max_length=15)  
    lab_count = models.IntegerField(default=0)  
    lab_description = models.CharField(max_length=200)

    class Meta:
        db_table = 'labdetails'


# FacultyDetails model
from django.db import models

class FacultyDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='id')
    name = models.CharField(max_length=100)  
    department = models.CharField(max_length=100)  
    lab_name = models.CharField(max_length=100) 
    lab_id = models.CharField(max_length=10) 
    mobile = models.CharField(max_length=10) 
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='faculty_images/', blank=True, null=True)  # New image field

    class Meta:
        db_table = 'facultydetails'

# StudentDetails model
class StudentDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='id')  
    name = models.CharField(max_length=100)  
    department = models.CharField(max_length=100)  
    lab_name = models.CharField(max_length=100) 
    lab_id = models.CharField(max_length=10) 
    mobile = models.CharField(max_length=10) 
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)  # New image field

    class Meta:
        db_table = 'studentdetails'
