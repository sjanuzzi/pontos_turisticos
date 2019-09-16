from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracoesSerializer
#from django_filters.rest_framework import DjangoFilterBackend

class AtracaoViewSet(ModelViewSet):

	queryset = Atracao.objects.all()
	serializer_class = AtracoesSerializer
#	filter_backends = (DjangoFilterBackend, ) # Retirar o REST_FRAMEWORK do setting
	filterset_fields = ['nome', 'descricao']