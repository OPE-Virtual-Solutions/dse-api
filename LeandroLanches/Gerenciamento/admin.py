
from django.contrib import admin
from .models import *

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = (
        'id_bairro',
        'nome_bairro', 
        'cidade', 
        'uf', 
        'taxa'
    )
    list_display_links = ["id_bairro"]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id_cliente',
        'nome_cliente', 
        'telefone'
    )
    list_display_links = ["id_cliente"]


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        'id_funcionario',
        'cargo',
    )
    list_display_links = ["id_funcionario"]


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        'id_endereco',
        'cep',
        'logradouro', 
        'numero', 
        'bairro', 
        'cliente'
    )
    list_display_links = ["id_endereco"]


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = (
        'id_ingrediente',
        'nome_ingrediente',
        'quantidade'
    )
    list_display_links = ["id_ingrediente"]


@admin.register(ItemPedido)
class ItemPedidoAmin(admin.ModelAdmin):
    list_display = (
        "id_item_pedido", 
        'produto', 
        'pedido',
        'quantidade', 
        'preco', 
        "ativo"
    )
    list_display_links = ["id_item_pedido"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id_pedido',
        'cliente', 
        'endereco', 
        'atendimento_presencial', 
        'valor_total',
        'metodo_pagamento', 
        'status',
        'criado_em',
        'finalizado_em',
        'funcionario'
    )
    list_display_links = ["id_pedido"]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'id_produto',
        'nome_produto',
        'preco', 
        'descricao', 
        'ativo',
        'categoria'
    )
    list_display_links = ["id_produto"]


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id_usuario',
        'nome_usuario',
        'email', 
        'senha', 
        'tipo'
    )
    list_display_links = ["id_usuario"]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'id_categoria',
        'nome_categoria',
        'ativo'
    )   
    list_display_links = ["id_categoria"]
