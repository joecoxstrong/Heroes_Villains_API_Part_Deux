from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypesSerializer
from super_types.models import SuperTypes
from rest_framework import status

from super_types import serializers


@api_view(['GET','POST'])
def super_types_list(request):
    if request.method == 'GET':
        super_type = SuperTypes.objects.all()
        serializer = SuperTypesSerializer(super_type, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperTypesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def super_types_detail(request, pk):
    super_type = get_object_or_404(SuperTypes, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypesSerializer(super_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperTypesSerializer(super_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

