from django.urls import path
from .views import *

from rest_framework import routers
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('bairros', BairroViewSet)
router.register('categorias', CategoriaViewSet)
router.register('clientes', ClienteViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('funcionarios', FuncionarioViewSet)
router.register('ingredientes', IngredienteViewSet)
router.register('produtos', ProdutoViewSet)
router.register('ingredientesProdutos', IngredienteProdutoViewSet)
router.register('itensPedidos', ItemPedidoViewSet)
router.register('pedidos', PedidoViewSet)
router.register('usuarios', UsuarioViewSet)


urlpatterns = [
    path('bairros/', BairroAPIView.as_view(), name='bairros'),
    path('clientes/', ClienteAPIView.as_view(), name='clientes'),
    path('ingredientes/', IngredienteAPIView.as_view(), name='ingredientes'),
    path('enderecos/', EnderecoAPIView.as_view(), name='enderecos'),
    path('ingredientesProdutos/', IngredienteProdutoAPIView.as_view(), name='ingredientesProdutos'),
    path('itensPedidos/', ItemPedidoAPIView.as_view(), name='itensPedidos'),
    path('pedidos/', PedidoAPIView.as_view(), name='pedidos'),
    path('produtos/', ProdutoAPIView.as_view(), name='produtos'),
    path('usuarios/', UsuarioAPIView.as_view(), name='usuarios'),
    path('categorias/', CategoriaAPIView.as_view(), name='categorias'),
]
