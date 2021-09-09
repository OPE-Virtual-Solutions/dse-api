from django.contrib import admin
from .models import *

@admin.register(TbBairro)
class TbBairroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'uf', 'taxa')


@admin.register(TbCliente)
class TbClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')


@admin.register(TbEndereco)
class TbEnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep','logradouro', 'numero', 'bairro', 'cliente')


@admin.register(TbIngrediente)
class TbIngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome','quantidade')


@admin.register(TbIngredienteProduto)
class TbIngredienteProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto','ingrediente')


@admin.register(TbItemPedido)
class TbItemPedidoAmin(admin.ModelAdmin):
    list_display = ('produto', 'pedido','quantidade', 'preco')


@admin.register(TbPedido)
class TbPedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'endereco', 'atendimento_presencial', 'valor_total',
        'metodo_pagamento', 'status','criado_em','finalizado_em','funcionario')


@admin.register(TbProduto)
class TbProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco', 'descricao', 'ativo','categoria')


@admin.register(TbUsuario)
class TbUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome','email', 'senha', 'tipo')


@admin.register(TbCategoria)
class TbCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','ativo')   
