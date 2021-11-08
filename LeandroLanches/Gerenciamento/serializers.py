
from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from datetime import date
from .models import *
from .serializers import *


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


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        categoria = serializers.SlugRelatedField(many=False, read_only=True, slug_field='nome_categoria')
        model = Produto
        fields = ('id_produto', 'nome_produto', 'preco', 'descricao', "quantidade", 'ativo', 'categoria', 'ingredientes')
        depth = 1 


class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(many = False)

    class Meta:
        model = ItemPedido
        fields = (
            'id_item_pedido',
            'produto',
            'pedido',
            'quantidade',
            'preco',
            'ativo',
        )
        # depth = 1

class CreateItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = (
            'id_item_pedido',
            'produto',
            'pedido',
            'quantidade',
            'usuario',
            'ativo',
            'preco'
        )


class GetPedidoSerializer(serializers.ModelSerializer):
    produtos = ItemPedidoSerializer(many  = True)

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
            'tipo_pedido',
            "observacao",
            'finalizado_em',
            'funcionario',
            'produtos'
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
            'tipo_pedido',
            'finalizado_em',
            "observacao",
            'funcionario',
        )


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id_ingrediente', 'nome_ingrediente', 'quantidade')


class CreateUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id_usuario',
            'nome_usuario',
            'email',
            'senha',
            'tipo',
        )

class UsuarioSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(many = False)
    cliente = ClienteSerializer(many = False)

    class Meta:
        model = Usuario
        fields = (
            'id_usuario',
            'nome_usuario',
            'email',
            'senha',
            'tipo',
            "cliente",
            "funcionario",
            "primeiro_acesso"
        )


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class RegistrarSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser'],
            is_active = validated_data['is_active'],
            password = validated_data['password'],
            date_joined = date.today()
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
