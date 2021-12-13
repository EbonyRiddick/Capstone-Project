from django.urls import path
from . import views 

app_name = "job_seeker"
urlpatterns =[
    path('', views.AllSeekers.as_view()),
    path('home/', views.SeekerRegistration.as_view()),
    path('SeekerProfile/<int:pk>', views.SeekerProfile.as_view()),
    # path('edit_profile/', views.edit_profile, name= 'edit_profile')

    
]