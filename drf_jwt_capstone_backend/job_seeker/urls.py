from django.urls import path
from . import views

app_name = "job_seeker"
urlpatterns =[
    path('SeekerProfile/', views.SeekerProfile.as_view()),
    # path('edit_profile/', views.edit_profile, name= 'edit_profile')
    
]