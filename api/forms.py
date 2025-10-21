from student.models import Student
from django import forms

class StudentApiForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'