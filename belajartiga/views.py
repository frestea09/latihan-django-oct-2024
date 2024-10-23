from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserBelajarTiga
from .serializer import UserBelajarTigaSerializer
# Create your views here.
@api_view(['GET'])
def get_data(request):
    userBelajarTiga = UserBelajarTiga.objects.all()
    dataUserBelajarTiga = UserBelajarTigaSerializer(userBelajarTiga, many=True).data
    return Response(dataUserBelajarTiga)
@api_view(['POST'])
def post_data(request):
    return Response(request.data)
    serializationuser = UserBelajarTigaSerializer(request.data)
    if serializationuser.is_valid():
        serializationuser.save()
        return Response(serializationuser.data, status=status.HTTP_201_CREATED)
    return Response(serializationuser.errors, status=400)
@api_view(['PUT'])
def update_user(request, pk):
    try:
        user = UserBelajarTiga.objects.get(pk=pk)
    except UserBelajarTiga.DoesNotExist:
        return Response(status=404)
    serializer = UserBelajarTigaSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = UserBelajarTiga.objects.get(pk=pk)
    except UserBelajarTiga.DoesNotExist:
        return Response(status=404)
    user.delete()
    return Response(status=204)
