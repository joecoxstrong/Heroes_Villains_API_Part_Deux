from rest_framework import serializers
from .models import Supers

class SuperSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Supers
        fields = ['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchprase', 'super_type', 'super_type_id']

    super_type_id = serializers.IntegerField(write_only = True)
         