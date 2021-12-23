
from django.http.response import Http404, HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from authentication.serializers import SeekerRegistrationSerializer
from . serializer import SeekerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
# from django.urls import reverse



class SeekerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        seeker = User.objects.all()
        serializer = SeekerSerializer(seeker, many=True)
        return Response(serializer.data)



# class SeekerRegistration(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         serializer = SeekerSerializer(data= request.data)
#         if serializer.isValid():
#             serializer.save()
#             return Response(serializer.data, status=status.Http_201_CREATED)
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)

class SeekerProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        zip_code = self.get_object(pk)
        serializer = SeekerRegistrationSerializer(zip_code)
        return Response(serializer.data)
    
    def put(self, request, pk):
        seeker = self.get_object(pk)
        serializer = SeekerSerializer(seeker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seeker = self.get_object(pk)
        seeker.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = SeekerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class EditSeeker(APIView):
#     permission_classes = [IsAuthenticated]

#     def update (request, user_id):
#         update_seeker= SeekerProfile.objects.get(id= user_id)
#         update_seeker.street = request.POST.get('street')
#         update_seeker.city = request.POST.get('city')
#         update_seeker.state = request.POST.get('state')
#         update_seeker.zip_code = request.POST.get('zip_code')
#         update_seeker.email = request.POST.get('email')
#         update_seeker.phone_number = request.POST.get('phone_number')
#         update_seeker.save()
#         return HttpResponseRedirect (reverse('job_seeker:SeekerProfile'))
