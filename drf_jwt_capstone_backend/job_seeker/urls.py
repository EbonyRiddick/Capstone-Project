from django.urls import path
from . import views

app_name = "job_seeker"
urlpatterns =[
    path('job_seeker/', views.SeekerList.as_view()),
]