
from django.urls import path
from . import views

app_name = 'student'  # Define the app_name here
urlpatterns = [
    
    path('view_student/', views.view_student, name='view_student'),
    path('add_student/', views.add_student, name='add_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    # other paths
]
