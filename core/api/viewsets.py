from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.models import Pontos_Turisticos
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response

class Ponto_TuristicoViewSet(ModelViewSet):

    #queryset = Pontos_Turisticos.objects.all()
    serializer_class = PontoTuristicoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )
    filter_backends = (SearchFilter, )
    search_fields = ('nome', 'descricao', 'enderecos__linha1')
    lookup_field = 'nome'  # tem que ser exclusive e unico no banco de dados

    def get_queryset(self):
        id = self.request.query_params.get('id', None) # com o get podemos trabalhar com o none caso o ID nao seja passado
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = Pontos_Turisticos.objects.all() # nao executa o select * from

        if id:
            queryset = Pontos_Turisticos.objects.filter(id=id)
        if nome:
            queryset = Pontos_Turisticos.objects.filter(nome__iexatc=nome)

        if descricao:
            queryset = Pontos_Turisticos.objects.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):# GET   # get retorna uma lista de objetos
        return super(Ponto_TuristicoViewSet, self).list(request, *args, **kwargs)
        #queryset = User.objects.all()
        #serializer = UserSerializer(queryset, many=True)
        #return Response(serializer.data)

    #    return Response({'teste':123})

    def create(self, request, *args, **kwargs):
        return super(Ponto_TuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(Ponto_TuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs): # get retorna apenas um objeto
        return super(Ponto_TuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):# kwargs é  PK
        return super(Ponto_TuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs): #path
        return super(Ponto_TuristicoViewSet, self).partial_update(request, *args, **kwargs)


    #@action(methods=['GET'], detail=True)  # decorators actions Detail = false cor\responde a uma action do endpoint e nao a um recurso
    #def denunciar(self, request, pk=None):
    #    pass
