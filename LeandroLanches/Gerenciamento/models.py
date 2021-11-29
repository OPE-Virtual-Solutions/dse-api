# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Bairro(models.Model):
    id = models.AutoField(db_column='id_bairro', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='nome_bairro', max_length=50, unique=True)  # Field name made lowercase.
    city = models.CharField(db_column="cidade", max_length=50)
    state = models.CharField(db_column="uf", max_length=2)
    tax = models.FloatField(db_column="taxa", blank=True, null=True)

    class Meta:
        db_table = 'TB_BAIRRO'


class Categoria(models.Model):
    id = models.AutoField(db_column='id_categoria', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='nome_categoria', max_length=50)  # Field name made lowercase.
    active = models.BooleanField(db_column="ativo", default = False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TB_CATEGORIA'


class Cliente(models.Model):
    id = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_cliente', primary_key=True)
    fullName = models.CharField(db_column='nome_cliente', max_length=50)  # Field name made lowercase.
    phone = models.CharField(db_column="telefone", max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'TB_CLIENTE'


class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    zipCode = models.CharField(db_column="cep", max_length=8)
    street = models.CharField(db_column="logradouro", max_length=50)
    number = models.IntegerField(db_column="numero", blank=True, null=True)
    district = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='bairro', blank=True, null=True)
    costumer = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')

    class Meta:
        db_table = 'TB_ENDERECO'


class Funcionario(models.Model):
    CARGO_FUNCIONARIO = [
        ("admin", "Administrador do sistema"),
        ("atendente", "Atendente"),
        ("estoquista", "Estoquista"),
    ]

    id = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_funcionario', primary_key=True)
    role = models.CharField(max_length=255, db_column='cargo', choices = CARGO_FUNCIONARIO, default = "atendente")

    class Meta:
        db_table = 'TB_FUNCIONARIO'


class Ingrediente(models.Model):
    id = models.AutoField(db_column='id_ingrediente', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='nome_ingrediente', max_length=50)  # Field name made lowercase.
    quantity = models.IntegerField(db_column = "quantidade")

    class Meta:
        db_table = 'TB_INGREDIENTE'


class ItemPedido(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_item_pedido")
    product = models.ForeignKey('Produto', models.DO_NOTHING, db_column='produto')
    order = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido', blank=True, null=True, related_name = "products")
    user = models.ForeignKey("Usuario", models.DO_NOTHING, db_column="usuario", blank = True, null = True)
    quantity = models.IntegerField(db_column="quantidade")
    price = models.FloatField(db_column="preco")
    active = models.BooleanField(default = True, db_column="ativo")  # Field name made lowercase.

    class Meta:
        db_table = 'TB_ITEM_PEDIDO'


class Pedido(models.Model):
    STATUS_PEDIDO = [
        ("aguardando", "Aguardando inicio do preparo"),
        ("em_andamento", "Em andamento"),
        ("pronto", "Pronto para despache"),
        ("finalizado", "Finalizado"),
        ("cancelado", "Cancelado")
    ]

    TIPOS_PEDIDO = [
        ("pra_viagem", "Pra viagem"),
        ("pra_consumir", "Pra consumir")
    ]

    id = models.AutoField(db_column='ID_PEDIDO', primary_key=True)  # Field name made lowercase.
    orderCode = models.CharField(max_length=8, blank=True, null=True)
    costumer = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    address = models.ForeignKey(Endereco, models.DO_NOTHING, db_column='endereco', blank=True, null=True)
    isLocalOrder = models.BooleanField(db_column="atendimento_presencial")
    totalPrice = models.FloatField(db_column="valor_total", blank=True, null=True)
    paymentMethod = models.CharField(db_column="metodo_pagamento", max_length=255)
    status = models.CharField(max_length=255, choices = STATUS_PEDIDO)
    createdAt = models.DateTimeField(db_column = "criado_em")
    note = models.CharField(db_column = "observacao", max_length = 280, null = True, blank = True)
    cancelNote = models.CharField(db_column = "motivo_cancelamento", max_length = 280, null = True, blank = True)
    finishedAt = models.DateTimeField(db_column = "finalizado_em", blank=True, null=True)
    employee = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='funcionario', blank=True, null=True)
    type = models.CharField(db_column='tipo_pedido', choices = TIPOS_PEDIDO, max_length=30, blank=True, null=True)
    
    class Meta:
        db_table = 'TB_PEDIDO'


class Produto(models.Model):
    id = models.AutoField(db_column='id_produto', primary_key=True)  # Field name made lowercase.
    # id = models.IntegerField()
    name = models.CharField(db_column="nome_produto", max_length=100)
    price = models.FloatField(db_column="preco")
    description = models.CharField(db_column="descricao", max_length=400, blank=True, null=True)
    active = models.BooleanField(db_column="ativo")
    quantity = models.IntegerField(db_column="quantidade", default = 0)
    category = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria', related_name="ingredients", blank=True, null=True)
    ingredients = models.ManyToManyField(Ingrediente, blank = True)

    class Meta:
        db_table = 'TB_PRODUTO'


class Usuario(models.Model):
    id = models.AutoField(db_column="id_usuario", primary_key=True)
    fullName = models.CharField(db_column="nome_completo", max_length=50)
    email = models.CharField(db_column="email", max_length=255, blank=True, null=True)
    password = models.CharField(db_column="senha", max_length=255, blank=True, null=True)
    type = models.CharField(db_column="tipo", max_length=255)
    firstAccess = models.BooleanField(db_column="primero_acesso", default = True)
    active = models.BooleanField(db_column="ativo", default = True)

    class Meta:
        db_table = 'TB_USUARIO'
