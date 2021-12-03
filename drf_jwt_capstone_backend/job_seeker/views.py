from django.shortcuts import render
from django.http.response import Http404
from rest_framework.permissions import IsAuthenticated
from . models import Seeker
from . serializer import SeekerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class SeekerList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        seeker = Seeker.objects.all()
        serializer = SeekerSerializer(seeker, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SeekerSerializer(data= request.data)
        if serializer.isValid():
            serializer.save()
            return Response(serializer.data, status=status.Http_201)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)