from django.urls import path
from . import views 

app_name = "job_poster"
urlpatterns =[
    path('', views.PosterView.as_view()),
    # path('new/', views.PosterRegistration.as_view()),
    path('<int:pk>/', views.PosterProfile.as_view()),
    # path('edit/', views.EditPoster.as_view(), name= 'edit_profile')
    
]