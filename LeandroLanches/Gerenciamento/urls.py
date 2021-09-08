from django.urls import path

from .views import *

urlpatterns = [
    path('bairros/', TbBairroAPIView.as_view(), name='bairros'),
    path('clientes/', TbClienteAPIView.as_view(), name='clientes'),
    path('ingredientes/', TbIngredienteAPIView.as_view(), name='ingredientes'),
    path('enderecos/', TbEnderecoAPIView.as_view(), name='enderecos'),
    path('ingredientesProdutos/', TbIngredienteProdutoAPIView.as_view(), name='ingredientesProdutos'),
    path('itensPedidos/', TbItemPedidoAPIView.as_view(), name='itensPedidos'),
    path('pedidos/', TbPedidoAPIView.as_view(), name='pedidos'),
    path('produtos/', TbProdutoAPIView.as_view(), name='produtos'),
    path('usuarios/', TbUsuarioAPIView.as_view(), name='usuarios'),
    path('categorias/', TbCategoriaAPIView.as_view(), name='categorias'),
]
