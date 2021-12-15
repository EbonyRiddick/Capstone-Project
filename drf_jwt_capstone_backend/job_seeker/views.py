
from django.http.response import Http404, HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from . models import SeekerProfile
from rest_framework.serializers import Serializer
from . serializer import SeekerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse



class AllSeekers(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        seeker = SeekerProfile.objects.all()
        serializer = SeekerSerializer(seeker, many=True, partial = True)
        return Response(serializer.data)



class SeekerRegistration(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = SeekerSerializer(data= request.data)
        if serializer.isValid():
            serializer.save()
            return Response(serializer.data, status=status.Http_201_CREATED)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)

class SeekerProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get_seeker_info(self, user_id):
        try:
            return SeekerProfile.objects.get(pk=user_id)
        except SeekerProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seeker = self.get_seeker_info(pk)
        serializer = SeekerSerializer(seeker)
        return Response(serializer.data)
    
    def put(self, request, pk):
        seeker = self.get_seeker_info(pk)
        serializer = SeekerSerializer(seeker, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seeker = self.get_seeker_info(pk)
        seeker.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class EditSeeker(APIView):
    permission_classes = [IsAuthenticated]

    def update (request, user_id):
        update_seeker= SeekerProfile.objects.get(id= user_id)
        update_seeker.street = request.POST.get('street')
        update_seeker.city = request.POST.get('city')
        update_seeker.state = request.POST.get('state')
        update_seeker.zip_code = request.POST.get('zip_code')
        update_seeker.email = request.POST.get('email')
        update_seeker.phone_number = request.POST.get('phone_number')
        update_seeker.save()
        return HttpResponseRedirect (reverse('job_seeker:SeekerProfile'))
