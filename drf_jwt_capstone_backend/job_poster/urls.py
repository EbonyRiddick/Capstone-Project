from django.urls import path
from . import views 

app_name = "job_poster"
urlpatterns =[
    path('', views.AllPosters.as_view()),
    path('home/', views.PosterRegistration.as_view()),
    path('PosterProfile/<int:pk>', views.PosterProfile.as_view()),
    # path('edit_profile/', views.edit_profile, name= 'edit_profile')

    
]