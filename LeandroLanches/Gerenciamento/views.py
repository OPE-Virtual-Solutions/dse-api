
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

from rest_framework.pagination import PageNumberPagination
"""
API V2
"""
class BairroViewSet(viewsets.ModelViewSet):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        cidade = serializer.initial_data['city']
        bairro = serializer.initial_data['name']
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

        produto = Produto.objects.filter(name__icontains = data["name"])
        if produto:
            return Response({}, status = status.HTTP_409_CONFLICT)

        categoria = Categoria.objects.get(id = data["category"])
        if not categoria:
            return Response({}, status = status.HTTP_404_NOT_FOUND)

        novo_produto = Produto.objects.create(
            name = data["name"],
            price = data["price"],
            description = data["description"],
            active = data["active"],
            quantity = data["quantity"],
            category = categoria
        )
    
        novo_produto.save()

        for ingrediente in data["ingredients"]:
            ingrediente_obj = Ingrediente.objects.get(id = ingrediente["id"])

            if ingrediente_obj:
                novo_produto.ingredients.add(ingrediente_obj)
        
        serializer = ProdutoSerializer(novo_produto)

        return Response(serializer.data)


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

    def list(self, request):
        userId = request.GET.get("user")
        if userId is None:
            return Response(status = status.HTTP_404_NOT_FOUND)

        itens_pedido = ItemPedido.objects.filter(user = userId, active = True)
        serializer = ItemPedidoSerializer(itens_pedido, many = True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        item_pedido = request.data
        print("~ quantity received:", item_pedido["quantity"])

        try:
            atual_item_pedido = ItemPedido.objects.get(
                user = item_pedido["user"],
                product = item_pedido["product"],
                active = True
            )
        except:
            atual_item_pedido = None

        produto = Produto.objects.get(
            id = item_pedido["product"]
        )

        item_pedido["price"] = produto.price
        item_pedido["active"] = True

        if atual_item_pedido is not None:
            item_pedido["quantity"] += atual_item_pedido.quantity

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

        pedidos = Pedido.objects.all().order_by(
            "-createdAt"
        )
        pedido_serializer = GetPedidoSerializer(pedidos, many = True)

        return Response(pedido_serializer.data)
            

    def create(self, request):
        id_usuario = request.data["user"]
        pedido = request.data["order"]

        pedido_serializer = PedidoSerializer(data = pedido)
        pedido_serializer.is_valid(raise_exception = True)

        pedido = pedido_serializer.create(pedido_serializer.validated_data)

        ItemPedido.objects.filter(
            user = id_usuario,
            active = True
        ).update(
            active = False,
            order = pedido.id
        )
        
        return Response(pedido_serializer.data, status = status.HTTP_201_CREATED)



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def list(self, request):
        tipos = ["cliente", "funcionario"]

        filtro_tipo = request.GET.get("tipo", None)
        if filtro_tipo != None and filtro_tipo not in tipos:
            return Response(status = status.HTTP_400_BAD_REQUEST)

        if filtro_tipo:
            usuarios = Usuario.objects.filter(
                type = filtro_tipo
            )
        else:
            usuarios = Usuario.objects.all()
                
        usuario_serializer = UsuarioSerializer(usuarios, many = True)
        
        pagination = PageNumberPagination()
        pagination.paginate_queryset(queryset = usuarios, request = request)
        pagination_response = pagination.get_paginated_response(usuario_serializer.data)

        return pagination_response

    def partial_update(self, request, pk = 0):
        usuario = Usuario.objects.get(id = pk)
        
        funcionario_serializer = None
        cliente_serializer = None
        if usuario.type == "funcionario" and "role" in request.data:
            funcionario = Funcionario.objects.get(id = pk)
            funcionario.role = request.data["role"]

            funcionario_serializer = FuncionarioSerializer(
                instance = funcionario,
                data = request.data,
                partial = True
            )
            funcionario_serializer.is_valid()
        elif usuario.type == "cliente" and "phone" in request.data:
            cliente = Cliente.objects.get(id = pk)
            cliente.phone = request.data["phone"]

            cliente_serializer = ClienteSerializer(
                instance = cliente,
                data = request.data,
                partial = True
            )
            cliente_serializer.is_valid()

        email = request.data["email"] if "email" in request.data else None
        
        if "password" in request.data:
            print("senha:", request.data["password"])
            print("email:", usuario.email)
            django_user = User.objects.get(
                username = usuario.email
            )

            django_user.set_password(request.data["password"])
            

        if email is not None:
            print("~ pass [email]")
            django_user = User.objects.get(
                username = usuario.email
            )

            django_user.email = email
            django_user.username = email

        serializer = UsuarioSerializer(
            instance = usuario,
            data = request.data,
            partial = True
        )

        serializer.is_valid(raise_exception = True)

        django_user.save()
        serializer.save()
        
        if funcionario_serializer != None: funcionario_serializer.save()
        if cliente_serializer != None: cliente_serializer.save()

        return Response(
            serializer.data
        )


        


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

    def post(self, request):
        user_types = ["funcionario", "cliente"]

        if request.data["type"] not in user_types:
            return Response(status = status.HTTP_400_BAD_REQUEST)

        usuario_serializer = CreateUsuarioSerializer(
            data = request.data
        )

        usuario_serializer.is_valid(
            raise_exception = True 
        )

        django_user = User(
            username = usuario_serializer.data["email"],
            email = usuario_serializer.data["email"],
            first_name = usuario_serializer.data["fullName"],
            is_superuser = False
        )

        django_user.set_password(usuario_serializer.data["password"])
        django_user.validate_unique()
        
        usuario = usuario_serializer.create(usuario_serializer.validated_data)

        if request.data["type"] == "funcionario":
            funcionario_serializer = FuncionarioSerializer(data =
                {
                    "id": usuario.id,
                    "role": request.data["role"]
                }
            )

            funcionario_serializer.is_valid()
            funcionario_serializer.save()
        elif request.data["type"] == "cliente":
            cliente_serializer = ClienteSerializer(data =
                {
                    "id": usuario.id,
                    "fullName": usuario_serializer.data["fullName"],
                    "phone": request.data["phone"]
                }
            )

            cliente_serializer.is_valid()
            cliente_serializer.save()

        django_user.save()
        
        return Response(
            usuario_serializer.data
        )


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format = None):
        print("~ requestdata:", request.data)

        auth_serializer = AuthTokenSerializer(data = request.data)
        auth_serializer.is_valid(raise_exception = True)

        django_user = auth_serializer.validated_data["user"]

        user = Usuario.objects.get(email = django_user)
        user_serializer = UsuarioSerializer(instance = user, many = False)

        if user.type == "funcionario":
            employee = Funcionario.objects.get(id = user.id)

            response = {
                "user": {
                    **user_serializer.data,
                    "role": employee.role
                }
            }
        elif user.type == "cliente":
            costumer = Cliente.objects.get(id = user.id)

            response = {
                "user": {
                    **user_serializer.data,
                    "telefone": costumer.telefone
                }
            }
        
        login(request, django_user)
        token = super(LoginAPI, self).post(request, format = None)

        return Response({
            **response,
            "token": token.data
        })

