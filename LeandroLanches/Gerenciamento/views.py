from django.views import generic
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action

from rest_framework import mixins
from rest_framework.serializers import Serializer

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status # Status dos métodos HTTP 
from .models import *
from .serializers import *

"""
API V1
"""
class BairroAPIView(APIView):
    """
    EndPoint de bairros
    """

    def get(self, request):
        bairros = Bairro.objects.all()
        serializer = TbBairroSerializer(bairros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbBairroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoriaAPIView(APIView):
    """
    EndPoint de categorias
    """

    def get(self, request):
        bairros = Categoria.objects.all()
        serializer = CategoriaSerializer(bairros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClienteAPIView(APIView):
    """
    EndPoint de clientes
    """

    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EnderecoAPIView(APIView):
    """
    EndPoint de endereços
    """

    def get(self, request):
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EnderecoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FuncionarioAPIView(APIView):
    """
    EndPoint de funcionários
    """

    def get(self, request):
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FuncionarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IngredienteAPIView(APIView):
    """
    EndPoint de ingredientes
    """

    def get(self, request):
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IngredienteProdutoAPIView(APIView):
    """
    EndPoint de Ingredientes do produto
    """

    def get(self, request):
        ingredientes_produto = TbIngredienteProduto.objects.all()
        serializer = IngredienteProdutoSerializer(ingredientes_produto, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredienteProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ItemPedidoAPIView(APIView):
    """
    EndPoint de Itens dos produtos
    """

    def get(self, request):
        itens_pedido = ItemPedido.objects.all()
        serializer = ItemPedidoSerializer(itens_pedido, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemPedidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PedidoAPIView(APIView):
    """
    EndPoint de pedidos
    """

    def get(self, request):
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProdutoAPIView(APIView):
    """
    EndPoint de produtos
    """

    def get(self, request):
        produtos = Produto.objects.prefetch_related("ingredientes")
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsuarioAPIView(APIView):
    """
    EndPoint de usuários
    """

    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


"""
API V2
"""


class BairroViewSet(viewsets.ModelViewSet):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer




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
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = CreateProdutoSerializer

    def retrieve(self, request, pk = None):
        produto = Produto.objects.get(id_produto = pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def list(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def destroy(self, request, pk = None):
        produto = Produto.objects.get(id_produto = pk)
        ingredientes_produto = IngredienteProduto.objects.filter(produto = produto)
        self.perform_destroy(ingredientes_produto)
        self.perform_destroy(produto)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class IngredienteProdutoViewSet(viewsets.ModelViewSet):
    queryset = IngredienteProduto.objects.all()
    serializer_class = IngredienteProdutoSerializer


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
