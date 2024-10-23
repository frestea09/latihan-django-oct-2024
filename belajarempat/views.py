from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserBelajarEmpat
from .serializer import UserBelajarEmpatSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_user(request):
    UserBelajarEmpatData = UserBelajarEmpat.objects.all()
    UserBelajarSerializarer = UserBelajarEmpatSerializer(UserBelajarEmpatData, many=True)
    # return Response("hello")
    return Response(UserBelajarSerializarer.data)
@api_view(['POST'])
def post_user(request):
    serializationuser = UserBelajarEmpatSerializer(data=request.data)
    if serializationuser.is_valid():
        serializationuser.save()
        return Response(serializationuser.data, status=status.HTTP_201_CREATED)

    #     return Response(serializationuser.data, status=status.HTTP_201_CREATED)
    return Response(serializationuser.data)
