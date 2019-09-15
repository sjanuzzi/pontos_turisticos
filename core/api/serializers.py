from rest_framework.serializers import ModelSerializer
from core.models import Pontos_Turisticos

class PontoTuristicoSerializer (ModelSerializer):
    class Meta:
        model = Pontos_Turisticos
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto')