from django.urls import path, include
from .views import ProjectList, UserDetailAPI, RegisterUserAPIView, UserLogin

urlpatterns = [
    path('projects', ProjectList.as_view()),
    # path('signup', UserCreate.as_view()),
    path('login/', UserLogin.as_view()),
    path("get_details",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    
]