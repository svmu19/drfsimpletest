from proyects.models import Proyect
from rest_framework import viewsets, permissions
from .serializers import ProyectSerualizer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectSerualizer