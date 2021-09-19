from rest_framework import serializers
from .models import *


class BairroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bairro
        fields = (
            'id_bairro',
            'nome_bairro',
            'cidade',
            'uf',
            'taxa',
        )

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = (
            'id_categoria',
            'nome_categoria',
            'ativo',
        )


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = (
            'id_cliente',
            'nome_cliente',
            'telefone',
        )


class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = (
            'id_endereco',
            'cep',
            'logradouro',
            'numero',
            'bairro',
            'cliente',
        )


class FuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcionario
        fields = (
            'id_funcionario',
            'cargo',
        )


class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingrediente
        fields = (
            "id_ingrediente",
            'nome_ingrediente',
            'quantidade'
        )


class IngredienteProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredienteProduto
        fields = (
            'id_ingrediente_produto',
            'produto',
            'ingrediente',
        )


class ItemPedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemPedido
        fields = (
            'id_item_pedido',
            'produto',
            'pedido',
            'quantidade',
            'preco'
        )


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = (
            'id_pedido',
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




class IngredienteProdutoRelatedSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(many = False, read_only = True)

    class Meta:
        model = IngredienteProduto
        fields = (
            "ingrediente",
        )
    
    def to_representation(self, instance):
        return {
            "id_ingrediente": instance.ingrediente.id_ingrediente,
            "nome": instance.ingrediente.nome_ingrediente,
            "quantidade": instance.ingrediente.quantidade
        }



class ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.SlugRelatedField(many=False, read_only=True, slug_field='nome_categoria')
    ingredientes = IngredienteProdutoRelatedSerializer(many = True)

    class Meta:
        model = Produto
        fields = (
            'id_produto',
            'nome_produto',
            'preco',
            'descricao',
            'ativo',
            'categoria',
            'ingredientes',
        )


class CreateProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'nome_produto',
            'preco',
            'descricao',
            'ativo',
            'categoria',
        )


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id_usuario',
            'nome_usuario',
            'email',
            'senha',
            'tipo',
        )
