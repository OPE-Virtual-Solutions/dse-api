
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
            'id',
            'name',
            'city',
            'state',
            'tax',
        )

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = (
            'id',
            'name',
            'active',
        )


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = (
            'id',
            'fullName',
            'phone',
        )


class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = (
            'id',
            'zipCode',
            'street',
            'number',
            'district',
            'costumer',
        )


class FuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcionario
        fields = (
            'id',
            'role',
        )


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='nome_categoria')
        model = Produto
        fields = (
            "id",
            "name",
            "price",
            "description",
            "active",
            "quantity",
            "category",
            "ingredients"
        )
        depth = 1 


class ItemPedidoSerializer(serializers.ModelSerializer):
    product = ProdutoSerializer(many = False)

    class Meta:
        model = ItemPedido
        fields = (
            'id',
            'product',
            'order',
            'quantity',
            'price',
            'active',
        )
        # depth = 1

class CreateItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = (
            'id',
            'product',
            'order',
            'quantity',
            'user',
            'active',
            'price'
        )


class GetPedidoSerializer(serializers.ModelSerializer):
    products = ItemPedidoSerializer(many  = True)

    class Meta:
        model = Pedido
        fields = (
            'id',
            'orderCode',
            'costumer',
            'address',
            'isLocalOrder',
            'totalPrice',
            'paymentMethod',
            'status',
            'createdAt',
            'type',
            "note",
            "cancelNote",
            "finishedAt",
            'employee',
            'products'
        )

class PedidoSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Pedido
        fields = (
            'id',
            'orderCode',
            'costumer',
            'address',
            'isLocalOrder',
            'totalPrice',
            'paymentMethod',
            'status',
            'createdAt',
            'type',
            'finishedAt',
            "cancelNote",
            "note",
            'employee',
        )


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = (
            "id",
            "name",
            "quantity"
        )


class CreateUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'fullName',
            'email',
            'password',
            'type',
        )

class UsuarioSerializer(serializers.ModelSerializer):
    employee = FuncionarioSerializer(many = False, source = "funcionario")
    costumer = ClienteSerializer(many = False, source = "cliente")

    class Meta:
        model = Usuario
        fields = (
            'id',
            'fullName',
            'email',
            'password',
            'type',
            "costumer",
            "employee",
            "firstAccess",
            "active"
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
