from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status # Status dos métodos HTTP 
from .models import *
from .serializers import *


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
        bairros = TbBairro.objects.all()
        serializer = TbBairroSerializer(bairros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbBairroSerializer(data=request.data)
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
