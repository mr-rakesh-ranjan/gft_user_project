from os import stat
from pickletools import read_uint1
from typing import ItemsView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from rest_framework import serializers
from rest_framework import status


# Create your views here.


@api_view(['GET'])
def ApiOverview(request):
    api_urls={
        'all_users' : '/',
        'get user by Id' : 'user/userId',
        'Add':'/create',
        'Update' : '/update/userId',
        'Delete' : 'user/userId/delete'
    }

    return Response(api_urls)


# Create user functions
@api_view(['POST'])
def add_user(request):
    user = UserSerializer(data=request.data)

    # for already exiting data
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This user is already exists')

    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# get all users
@api_view(['GET'])
def all_users(request):
    # parameters from URL
    if request.query_params:
        users = User.objects.filter(**request.query_param.dict())
    else:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

    # for error handing
    if users:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# get user by Id
@api_view(['GET'])
def get_userById(request, userId):
    user = User.objects.get(pk=userId)
    serializer = UserSerializer(user)
    if user:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



# update user
@api_view(['POST'])
def update_user(request, userId):
    user = User.objects.get(pk=userId)
    data = UserSerializer(instance=user, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# delete user
@api_view(['DELETE'])
def delete_user(request, userId):
    # user = get_object_or_404(User, pk=userId)
    user = User.objects.get(pk=userId)
    user.delete()
    return Response(status=status.HTTP_202_ACCEPTED)