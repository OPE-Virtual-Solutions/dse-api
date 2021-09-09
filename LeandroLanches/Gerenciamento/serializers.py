from rest_framework import serializers
from .models import *


class TbBairroSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbBairro
        fields = (
            'id',
            'nome',
            'cidade',
            'uf',
            'taxa',
        )


class TbCategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbCategoria
        fields = (
            'id',
            'nome',
            'ativo',
        )


class TbClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbCliente
        fields = (
            'id',
            'nome',
            'telefone',
        )


class TbEnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbEndereco
        fields = (
            'cep',
            'logradouro',
            'numero',
            'bairro',
            'cliente',
        )


class TbFuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbFuncionario
        fields = (
            'id',
            'cargo',
        )


class TbIngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbIngrediente
        fields = (
            "id",
            'nome',
            'quantidade'
        )


class TbIngredienteProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbIngredienteProduto
        fields = (
            'produto',
            'ingrediente',
        )


class TbItemPedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbItemPedido
        fields = (
            'id',
            'produto',
            'pedido',
            'quantidade',
            'preco'
        )


class TbPedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbPedido
        fields = (
            'codigo_pedido',
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


class TbIngredienteProdutoRelatedSerializer(serializers.ModelSerializer):
    ingrediente = TbIngredienteSerializer(many = False)

    class Meta:
        model = TbIngredienteProduto
        fields = (
            "ingrediente",
        )
    
    def to_representation(self, instance):
        return {
            "id": instance.ingrediente.id,
            "nome": instance.ingrediente.nome,
            "quantidade": instance.ingrediente.quantidade
        }



class TbProdutoSerializer(serializers.ModelSerializer):
    categoria = TbCategoriaSerializer()
    ingredientes = TbIngredienteProdutoRelatedSerializer(many = True)

    class Meta:
        model = TbProduto
        fields = (
            'id',
            'nome',
            'preco',
            'descricao',
            'ativo',
            'categoria',
            "ingredientes"
        )


class TbUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbUsuario
        fields = (
            'id',
            'nome',
            'email',
            'senha',
            'tipo',
        )
