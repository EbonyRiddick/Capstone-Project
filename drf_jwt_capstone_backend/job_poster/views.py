from django.http.response import Http404, HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from . models import PosterProfile
from rest_framework.serializers import Serializer
from . serializer import PosterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()




class AllPosters(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        poster = PosterProfile.objects.all()
        serializer = PosterSerializer(poster, many=True)
        return Response(serializer.data)



class PosterRegistration(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PosterSerializer(data= request.data)
        if serializer.isValid():
            serializer.save()
            return Response(serializer.data, status=status.Http_201_CREATED)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)

class PosterProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get_poster_info(self, pk):
        try:
            return PosterProfile.objects.get(pk=pk)
        except PosterProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        poster = self.get_poster_info(pk)
        serializer = PosterSerializer(poster)
        return Response(serializer.data)
    
    def put(self, request, pk):
        poster = self.get_poster_info(pk)
        serializer = PosterSerializer(poster, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        poster = self.get_poster_info(pk)
        poster.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)