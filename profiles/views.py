from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from . import serializers
from rest_framework.permissions import IsAuthenticated




class ProfileViewSet(viewsets.ViewSet):
    serializer_class = serializers.ProfileSerializer


    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = serializers.ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data.update({'success_message': 'your account created successfully'})
            # new_profile = UserProfile(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
            # new_profile.save()
            return Response(data)
        return status.HTTP_400_BAD_REQUEST

    def update(self, request, pk):
        instance = UserProfile.objects.get(id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data.update({'success_message': 'your account updated successfully'})
            return Response(data)
        return status.HTTP_400_BAD_REQUEST

    def retrieve(self, request, pk):
        queryset = UserProfile.objects.get(id=pk)
        serializer = serializers.ProfileSerializer(queryset, many=False)
        return Response(serializer.data)

    def destroy(self, request, pk):
        user = UserProfile.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

