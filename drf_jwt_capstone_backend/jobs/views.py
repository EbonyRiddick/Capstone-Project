from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status
from .models import JobListings
from .serializers import JobListingsSerializer, JobListingsDetailSerializer
from datetime import datetime, timezone, timedelta
from rest_framework.permissions import IsAuthenticated
from django.http.response import Http404

class JobsListingsView(APIView):
    def get(self, request):
        listings =JobListings.objects.all()
        serializer = JobListingsSerializer(listings, many=True)
        return Response(serializer.data)

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

class ListingCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = JobListingsDetailSerializer (data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.Http_201_CREATED)
        return Response (serializer.errors, status = status.Http_400_BAD_REQUEST)



class JobListingsDetailsView(APIView):
    def get_object(self, pk):
        try:
            return JobListings.objects.get(pk=pk)
        except JobListings.DoesNotExist:
            raise Http404

    



    





