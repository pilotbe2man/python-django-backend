# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .models import Firstapp
from .serializers import FirstappSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class ListFirstappsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Firstapp.objects.all()
    serializer_class = FirstappSerializer

class FirstappCreate(APIView):
    """
    Retrieve a booking instance.
    """
    def post(self, request, format=None):
        title=request.data['title']
        description = request.data['description']
        firstapp = Firstapp.objects.create(title=title, description=description)
        firstapp.save

        data = {
            'id': firstapp.id,
        }
        return Response(data, status=status.HTTP_200_OK)


class FirstappDetail(APIView):
    """
    Retrieve a firstapp instance.
    """
    def get_object(self, pk):
        try:
            return Firstapp.objects.get(pk=pk)
        except Firstapp.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        firstapp = self.get_object(pk)
        serializer = FirstappSerializer(firstapp)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        firstapp = self.get_object(pk)
        serializer = FirstappSerializer(firstapp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        firstapp = self.get_object(pk)
        firstapp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)