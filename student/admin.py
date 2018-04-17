from django.contrib import admin

# Register your models here.
from student.models import College, Student

admin.site.register([Student, College])
