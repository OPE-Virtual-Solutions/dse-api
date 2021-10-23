
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import serializers, status # Status dos métodos HTTP 
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.permissions import AllowAny
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

"""
API V2
"""
class BairroViewSet(viewsets.ModelViewSet):
    queryset = Bairro.objects.all()
    print('teste',queryset)
    serializer_class = BairroSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        cidade = serializer.initial_data['cidade']
        bairro = serializer.initial_data['nome_bairro']
        lista_cidade = ['Barueri']
        lista_bairros = ['Jd Isaura', 'Pq Santana']
        # print("oiiii",Bairro.objects.filter(nome_bairro=bairro).exists())
        if (cidade in lista_cidade or bairro in lista_bairros):
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            # print(serializer.data)
            headers = self.get_success_headers(serializer.data)
        else:
            raise Exception
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()


class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data

        novo_produto = Produto.objects.create(
            nome_produto = data["nome_produto"],
            preco = data["preco"],
            descricao = data["descricao"],
            ativo = data["ativo"]
        )
    
        novo_produto.save()

        for ingrediente in data["ingredientes"]:
            ingrediente_obj = Ingrediente.objects.get(nome_ingrediente=ingrediente["nome_ingrediente"])
            print(ingrediente,ingrediente_obj)
            novo_produto.ingredientes.add(ingrediente_obj)
        
        serializer = ProdutoSerializer(novo_produto)

        return Response(serializer.data)


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['confirmado'] = 0
        print(serializer)
        if serializer.initial_data['pedido'] is not None:
            serializer.initial_data['confirmado'] = 1
        print(serializer.initial_data['confirmado'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

'''class GrupoViewSet(viewsets.ModelViewSet):
    permission_classes = (  GrupoAdmin,
                            permissions.DjangoModelPermissions,)
    queryset = AuthGroup.objects.all()
    serializer_class = GrupoSerializer
'''


class RegistrarViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrarSerializer

    def list(self, request, *args, **kwargs):
        msg = {"mensagem":"Bem-vindo registre-se"}
        return JsonResponse(msg)
    
    def retrieve(self, request, *args, **kwargs):
        msg = {"mensagem":"Não é possivel acessar a página"}
        return JsonResponse(msg)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": RegistrarSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
