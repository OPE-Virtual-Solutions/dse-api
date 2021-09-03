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


class TbProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbProduto
        fields = (
            'nome',
            'preco',
            'descricao',
            'ativo',
            'categoria',
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