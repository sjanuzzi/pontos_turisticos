from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import Pontos_Turisticos
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response

class Ponto_TuristicoViewSet(ModelViewSet):

    #queryset = Pontos_Turisticos.objects.all()
    serializer_class = PontoTuristicoSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]

    #def get_queryset(self):
    #    return Pontos_Turisticos.objects.filter(aprovado=True)

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
