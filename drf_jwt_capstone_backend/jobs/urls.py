from django.urls import path
from . import views 

app_name = "jobs"
urlpatterns =[
    path('', views.JobsListingsView.as_view()),
    path('create/', views.ListingCreate.as_view()),
    path('<int:pk>/', views.JobListingsDetailsView.as_view()),
    # path('search/', views.JobSearchView.as_view())

    
]