
from django.contrib import admin
from .models import *

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome_bairro', 'cidade', 'uf', 'taxa')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'telefone')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cargo',)


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep','logradouro', 'numero', 'bairro', 'cliente')


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome_ingrediente','quantidade')


@admin.register(ItemPedido)
class ItemPedidoAmin(admin.ModelAdmin):
    list_display = ('produto', 'pedido','quantidade', 'preco')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'endereco', 'atendimento_presencial', 'valor_total',
        'metodo_pagamento', 'status','criado_em','finalizado_em','funcionario')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto','preco', 'descricao', 'ativo','categoria')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_usuario','email', 'senha', 'tipo')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria','ativo')   
