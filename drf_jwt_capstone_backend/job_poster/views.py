from django.http.response import Http404, HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from . models import PosterProfile
from rest_framework.serializers import Serializer
from . serializer import PosterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from authentication.serializers import PosterRegistrationSerializer



class PosterView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        poster = User.objects.all()
        serializer = PosterSerializer(poster, many=True)
        return Response(serializer.data)



# class PosterRegistration(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         serializer = PosterSerializer(data= request.data)
#         if serializer.isValid():
#             serializer.save()
#             return Response(serializer.data, status=status.Http_201_CREATED)
#         return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)

class PosterProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        company_name = self.get_object(pk)
        serializer = PosterRegistrationSerializer(company_name)
        return Response(serializer.data)
    
    def put(self, request, pk):
        poster = self.get_object(pk)
        serializer = PosterSerializer(poster, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        poster = self.get_object(pk)
        poster.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# class EditPoster(APIView):
#     permission_classes = [IsAuthenticated]

#     def update (request, user_id):
#         update_poster= PosterProfile.objects.get(id= user_id)
#         update_poster.company_name = request.POST.get('company_name')
#         update_poster.email = request.POST.get('email')
#         update_poster.phone_number = request.POST.get('phone_number')
#         update_poster.save()
#         return HttpResponseRedirect (reverse('job_poster:PosterProfile'))


