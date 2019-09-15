from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentarios
from .serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
	queryset = Comentarios.objects.all()
	serializer_class = ComentarioSerializer