
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

    def list(self, request):
        userId = request.GET.get("user", 1)

        itens_pedido = ItemPedido.objects.filter(usuario = userId, ativo = True)
        serializer = ItemPedidoSerializer(itens_pedido, many = True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        item_pedido = request.data

        try:
            atual_item_pedido = ItemPedido.objects.get(
                usuario = item_pedido["usuario"],
                produto = item_pedido["produto"],
                ativo = True
            )
        except:
            atual_item_pedido = None

        produto = Produto.objects.get(
            id_produto = item_pedido["produto"]
        )

        item_pedido["preco"] = produto.preco
        item_pedido["ativo"] = True

        if atual_item_pedido is not None:
            item_pedido["quantidade"] += atual_item_pedido.quantidade

        serializer = CreateItemPedidoSerializer(data = item_pedido)

        serializer.is_valid(raise_exception = True)

        status_code = status.HTTP_200_OK

        if atual_item_pedido is not None:
            serializer.update(
                atual_item_pedido,
                serializer.validated_data
            )
        else:
            status_code = status.HTTP_201_CREATED

            serializer.create(
                serializer.validated_data
            )

        return Response(
            serializer.data,
            status = status_code
        )


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def list(self, request):
        filtro_atendimento = request.GET.get("apenasAtendimento", False)

        if filtro_atendimento:
            pedidos = Pedido.objects.exclude(
                status__in = ["finalizado", "cancelado"],
            )
            pedido_serializer = GetPedidoSerializer(pedidos, many = True)

            return Response(pedido_serializer.data)

        pedidos = Pedido.objects.all()
        pedido_serializer = GetPedidoSerializer(pedidos, many = True)

        return Response(pedido_serializer.data)
            

    def create(self, request):
        id_usuario = request.data["usuario"]
        pedido = request.data["pedido"]

        pedido_serializer = PedidoSerializer(data = pedido)
        pedido_serializer.is_valid(raise_exception = True)

        pedido = pedido_serializer.create(pedido_serializer.validated_data)

        ItemPedido.objects.filter(
            usuario = id_usuario,
            ativo = True
        ).update(
            ativo = False,
            pedido = pedido.id_pedido
        )
        
        return Response(pedido_serializer.data, status = status.HTTP_201_CREATED)



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
