
from django.contrib import admin
from .models import *

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name', 
        'city', 
        'state', 
        'tax'
    )
    list_display_links = ["id"]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fullName', 
        'phone'
    )
    list_display_links = ["id"]


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'role',
    )
    list_display_links = ["id"]


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'zipCode',
        'street', 
        'number', 
        'district', 
        'costumer'
    )
    list_display_links = ["id"]


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'quantity'
    )
    list_display_links = ["id"]


@admin.register(ItemPedido)
class ItemPedidoAmin(admin.ModelAdmin):
    list_display = (
        "id", 
        'product', 
        'order',
        'quantity', 
        'price', 
        "active"
    )
    list_display_links = ["id"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'costumer', 
        'address', 
        'isLocalOrder', 
        'totalPrice',
        'paymentMethod', 
        'status',
        'createdAt',
        'finishedAt',
        'employee'
    )
    list_display_links = ["id"]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price', 
        'description', 
        'active',
        'category'
    )
    list_display_links = ["id"]


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fullName',
        'email', 
        'password', 
        'type'
    )
    list_display_links = ["id"]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'active'
    )   
    list_display_links = ["id"]
