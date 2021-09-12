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
class TbBairroAPIView(APIView):
    """
    EndPoint de bairros
    """

    def get(self, request):
        bairros = TbBairro.objects.all()
        serializer = TbBairroSerializer(bairros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbBairroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbCategoriaAPIView(APIView):
    """
    EndPoint de categorias
    """

    def get(self, request):
        bairros = TbCategoria.objects.all()
        serializer = TbCategoriaSerializer(bairros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbCategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbClienteAPIView(APIView):
    """
    EndPoint de clientes
    """

    def get(self, request):
        clientes = TbCliente.objects.all()
        serializer = TbClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbEnderecoAPIView(APIView):
    """
    EndPoint de endereços
    """

    def get(self, request):
        enderecos = TbEndereco.objects.all()
        serializer = TbEnderecoSerializer(enderecos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbEnderecoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbFuncionarioAPIView(APIView):
    """
    EndPoint de funcionários
    """

    def get(self, request):
        funcionarios = TbFuncionario.objects.all()
        serializer = TbFuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbFuncionarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbIngredienteAPIView(APIView):
    """
    EndPoint de ingredientes
    """

    def get(self, request):
        ingredientes = TbIngrediente.objects.all()
        serializer = TbIngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbIngredienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbIngredienteProdutoAPIView(APIView):
    """
    EndPoint de Ingredientes do produto
    """

    def get(self, request):
        ingredientes_produto = TbIngredienteProduto.objects.all()
        serializer = TbIngredienteProdutoSerializer(ingredientes_produto, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbIngredienteProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbItemPedidoAPIView(APIView):
    """
    EndPoint de Itens dos produtos
    """

    def get(self, request):
        itens_pedido = TbItemPedido.objects.all()
        serializer = TbItemPedidoSerializer(itens_pedido, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbItemPedidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbPedidoAPIView(APIView):
    """
    EndPoint de pedidos
    """

    def get(self, request):
        pedidos = TbPedido.objects.all()
        serializer = TbPedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbPedidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbProdutoAPIView(APIView):
    """
    EndPoint de produtos
    """

    def get(self, request):
        produtos = TbProduto.objects.prefetch_related("ingredientes")
        serializer = TbProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbCreateProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TbUsuarioAPIView(APIView):
    """
    EndPoint de usuários
    """

    def get(self, request):
        usuarios = TbUsuario.objects.all()
        serializer = TbUsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbUsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


"""
API V2
"""


class TbBairroViewSet(viewsets.ModelViewSet):
    queryset = TbBairro.objects.all()
    serializer_class = TbBairroSerializer


class TbCategoriaViewSet(viewsets.ModelViewSet):
    queryset = TbCategoria.objects.all()
    serializer_class = TbCategoriaSerializer


class TbClienteViewSet(viewsets.ModelViewSet):
    queryset = TbCliente.objects.all()
    serializer_class = TbClienteSerializer


class TbEnderecoViewSet(viewsets.ModelViewSet):
    queryset = TbEndereco.objects.all()
    serializer_class = TbEnderecoSerializer


class TbFuncionarioViewSet(viewsets.ModelViewSet):
    queryset = TbFuncionario.objects.all()
    serializer_class = TbFuncionarioSerializer


class TbIngredienteViewSet(viewsets.ModelViewSet):
    queryset = TbIngrediente.objects.all()
    serializer_class = TbIngredienteSerializer


class TbProdutoViewSet(viewsets.ModelViewSet):
    queryset = TbProduto.objects.all()
    serializer_class = TbProdutoSerializer


class TbIngredienteProdutoViewSet(viewsets.ModelViewSet):
    queryset = TbIngredienteProduto.objects.all()
    serializer_class = TbIngredienteProdutoSerializer


class TbItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = TbItemPedido.objects.all()
    serializer_class = TbItemPedidoSerializer


class TbPedidoViewSet(viewsets.ModelViewSet):
    queryset = TbPedido.objects.all()
    serializer_class = TbPedidoSerializer


class TbUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TbUsuario.objects.all()
    serializer_class = TbUsuarioSerializer
