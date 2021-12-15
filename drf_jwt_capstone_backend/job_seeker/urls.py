from django.urls import path
from . import views 

app_name = "job_seeker"
urlpatterns =[
    path('', views.AllSeekers.as_view()),
    # path('new/', views.SeekerRegistration.as_view()),
    path('seeker/<int:pk>', views.SeekerProfile.as_view()),
    path('edit/', views.EditSeeker.as_view(), name= 'edit_profile')

    
]