from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import Pontos_Turisticos
from atracoes.api.serializers import AtracoesSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecosSerializers

class PontoTuristicoSerializer (ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    enderecos = EnderecosSerializers()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = Pontos_Turisticos
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios','avaliacoes','enderecos','descricao_completa','descricao_completa2')

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

