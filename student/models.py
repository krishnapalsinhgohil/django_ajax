from django.db import models


class College(models.Model):
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name


class Student(models.Model):
    student_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    college_name = models.ForeignKey(College, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.student_name
