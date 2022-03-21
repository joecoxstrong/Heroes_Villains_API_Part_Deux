from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Supers



@api_view(['GET'])
def super_list(request):
    supers = Supers.objects.all()


    return Response('ok')

