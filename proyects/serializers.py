from rest_framework import serializers
from .models import Proyect

class ProyectSerualizer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)