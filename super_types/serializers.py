from dataclasses import fields
from rest_framework import serializers
from .models import SuperTypes

class SuperTypesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SuperTypes
        fields = ['type']
        