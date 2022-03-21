from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Supers
from .models import SuperTypes
from django.shortcuts import get_object_or_404



@api_view(['GET','POST'])
def super_list(request):
    
    

    if request.method == 'GET':
        supers = Supers.objects.all()
        super_types_param = request.query_params.get('type')
        
        
        if super_types_param:
            supers = supers.filter(super_type__type = super_types_param)
            serializer=SuperSerializer(supers,many=True)    
            return Response(serializer.data)
      
                
        else:
            super_types = SuperTypes.objects.all()
            custom_response_dictionary = {}

            for super_type in super_types:
                supers = Supers.objects.filter(super_type__type = super_type.type)

                super_serializer = SuperSerializer(supers, many = True)
                custom_response_dictionary[super_type.type] = super_serializer.data    

            return Response(custom_response_dictionary)


    elif request.method == 'POST':
        serilaizer = SuperSerializer(data=request.data)
        serilaizer.is_valid(raise_exception=True)
        serilaizer.save()
        return Response(serilaizer.data, status=status.HTTP_201_CREATED)    


@api_view(['GET','PUT','DELETE'])
def super_detail(request,pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
