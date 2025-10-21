from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='student_profile',
    null=True,
    blank=True
)


    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    username = models.CharField(max_length=100, unique=True)
    age = models.PositiveIntegerField()
    institution = models.CharField(max_length=155)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    year_of_study = models.PositiveIntegerField()
    about_student = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.institution})"

    class Meta:
        ordering = ['-created_at']