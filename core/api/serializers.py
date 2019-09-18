from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import Pontos_Turisticos, DocIdentificacao, Atracao
from atracoes.api.serializers import AtracoesSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecosSerializers
#from atracoes.models import Atracao
from enderecos.models import Endereco


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer (ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    #comentarios = ComentarioSerializer(many=True)
    #avaliacoes = AvaliacaoSerializer(many=True)
    enderecos = EnderecosSerializers()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = Pontos_Turisticos
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios','avaliacoes','enderecos','descricao_completa','descricao_completa2','doc_identificacao')
        read_only_fields = ('comentarios', 'avaliacoes')


    def cria_atracoes(self, atracoes, ponto): # many to many
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['enderecos']
        del validated_data['enderecos']


        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)


        ponto = Pontos_Turisticos.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco) # esta salvo no banco de dados e nao estra atrelado ao ponto
        ponto.enderecos = end # vincula o endereco ao ponto turistico
        ponto.doc_identificacao = doci
        ponto.save()

        return ponto


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

