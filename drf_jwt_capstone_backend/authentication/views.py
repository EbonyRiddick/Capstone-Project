from django.contrib.auth import get_user_model
from django.http.response import Http404
from .serializers import RegistrationSerializer, SeekerRegistrationSerializer, PosterRegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

class SeekerRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SeekerRegistrationSerializer


class PosterRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PosterRegistrationSerializer
