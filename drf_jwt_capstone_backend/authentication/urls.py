from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, PosterRegisterView,SeekerRegisterView

app_name = "authentication"
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/job_seeker/', SeekerRegisterView.as_view()),
    path('register/job_poster/', PosterRegisterView.as_view()),
]
