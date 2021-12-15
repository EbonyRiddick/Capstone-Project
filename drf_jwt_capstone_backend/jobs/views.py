from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import JobListings
from .serializers import JobListingsSerializer, JobListingsDetailSerializer
from datetime import datetime, timezone, timedelta
from django.contrib.auth import get_user_model

User = get_user_model()


class JobsListingsView(APIView):
    queryset = JobListings.objects.order_by('start_date').filter(is_active=True)
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobListingsSerializer

class ListingCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        data = self.request.data

        job_title = data['job_title']
        company_name = data['company_name']
        description = data['description']
        zip_code = ['zip_code']
        wage = data['wage']
        start_date= data['start_date']
        end_date= data['end_date']
  
        try:
            print(".............")
            print(company_name)

            listing = JobListings(
                title=job_title, 
                company=company_name,
                zip_code = zip_code ,
                wage=wage,
                start_date=start_date, 
                end_date=end_date,
                description=description)

            listing.save(force_insert=True)
            return Response({'success': "Success"})
            
        except Exception as e:
            return Response({'error': e})


class JobListingsDetailsView(APIView):
    queryset = JobListings.objects.order_by('start_date').filter(is_active=True)
    serializer_class = JobListingsDetailSerializer
    
class JobSearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobListingsSerializer

    def post(self, request):
        queryset = JobListings.objects.order_by('start_date').filter(is_active=True)
        data = request.data

        company_name = data['company_name']
        queryset = queryset.filter(company_name__iexact=company_name)

        zip_code = data['zip_code']
        queryset = queryset.filter(zip_code__iexact=zip_code)

        wage = data['wage']
        if wage == '$0+':
            wage = 0
        elif wage == '$7.50+':
            wage = 750
        elif wage == '$8.00+':
            wage = 800
        elif wage == '$9.00+':
            wage = 900
        elif wage == '$10.50+':
            wage = 1050
        elif wage == '$20.00+':
            wage = 2000
        elif wage == 'Any':
            wage = -1

        if wage != -1:
            queryset = queryset.filter(wage__gte=wage)





