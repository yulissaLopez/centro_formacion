from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import AllowAny


class UserList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


