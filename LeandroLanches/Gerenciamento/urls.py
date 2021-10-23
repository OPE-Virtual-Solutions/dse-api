from django.urls import path
from .views import *

from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter
from knox import views as knox_views


router = SimpleRouter()
router.register('bairros', BairroViewSet)
router.register('categorias', CategoriaViewSet)
router.register('clientes', ClienteViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('funcionarios', FuncionarioViewSet)
router.register('ingredientes', IngredienteViewSet)
router.register('produtos', ProdutoViewSet)
router.register('itensPedidos', ItemPedidoViewSet)
router.register('pedidos', PedidoViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('registrar-se', RegistrarViewSet)


urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
]
