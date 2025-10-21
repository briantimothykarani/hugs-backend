from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import (
    CurrentUserAPIView,
    StudentApiListCreate,
    StudentDelete,
    StudentListCreate,
    StudentUpdate,
    UserRegisterAPIView,
    csrf_cookie_view,
)

urlpatterns = [
    path('StudentApiListCreate/', StudentApiListCreate.as_view(), name='student-list-create'),
    path('StudentListCreate/', StudentListCreate.as_view(), name='student-list-all'),
    path('StudentUpdate/<int:id>/', StudentUpdate.as_view(), name='student-update'),
    path('StudentDelete/<int:pk>/', StudentDelete.as_view(), name='student-delete'),
    path('current_user/', CurrentUserAPIView.as_view(), name='current-user'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('csrf/', csrf_cookie_view, name='csrf-cookie'),
]