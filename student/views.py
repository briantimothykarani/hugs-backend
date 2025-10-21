from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
from .models import Student

def view_student(request):
    students = Student.objects.all()
    return render(request, 'view_student.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:view_student')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student:view_student')
    return render(request, 'delete_student.html', {'student': student})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:view_student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})
