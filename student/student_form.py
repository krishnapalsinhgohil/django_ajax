from django import forms

from student.models import College


class StudentForm(forms.Form):
    college = forms.ModelChoiceField(College.objects.all(), empty_label="Select college")
