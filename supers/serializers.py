from rest_framework import serializers
from .models import Supers


class SuperSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Supers
        fields = ['name', 'alter_ego', 'catchphrase', 'super_type', 'super_type_id', 'powers']
        depth = 1

    super_type_id = serializers.IntegerField(write_only = True)
         