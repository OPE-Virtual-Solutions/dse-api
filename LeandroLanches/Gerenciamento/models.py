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
    id_bairro = models.AutoField(db_column='ID_BAIRRO', primary_key=True)  # Field name made lowercase.
    nome_bairro = models.CharField(db_column='NOME_BAIRRO', max_length=50, unique=True)  # Field name made lowercase.
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    taxa = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'TB_BAIRRO'


class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='ID_CATEGORIA', primary_key=True)  # Field name made lowercase.
    nome_categoria = models.CharField(db_column='NOME_CATEGORIA', max_length=50)  # Field name made lowercase.
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome_categoria

    class Meta:
        db_table = 'TB_CATEGORIA'


class Cliente(models.Model):
    id_cliente = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_cliente', primary_key=True)
    nome_cliente = models.CharField(db_column='NOME_CLIENTE', max_length=50)  # Field name made lowercase.
    telefone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'TB_CLIENTE'


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='bairro', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')

    class Meta:
        db_table = 'TB_ENDERECO'


class Funcionario(models.Model):
    id_funcionario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_funcionario', primary_key=True)
    cargo = models.CharField(max_length=255)

    class Meta:
        db_table = 'TB_FUNCIONARIO'


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(db_column='ID_INGREDIENTE', primary_key=True)  # Field name made lowercase.
    nome_ingrediente = models.CharField(db_column='NOME_INGREDIENTE', max_length=50)  # Field name made lowercase.
    quantidade = models.IntegerField()

    class Meta:
        db_table = 'TB_INGREDIENTE'


class ItemPedido(models.Model):
    id_item_pedido = models.AutoField(primary_key=True)
    produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='produto')
    pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido', blank=True, null=True, related_name = "produtos")
    usuario = models.ForeignKey("Usuario", models.DO_NOTHING, db_column="usuario", blank = True, null = True)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    ativo = models.BooleanField(default = True)  # Field name made lowercase.

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

    id_pedido = models.AutoField(db_column='ID_PEDIDO', primary_key=True)  # Field name made lowercase.
    codigo_pedido = models.CharField(max_length=8, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, db_column='endereco', blank=True, null=True)
    atendimento_presencial = models.BooleanField()
    valor_total = models.FloatField(blank=True, null=True)
    metodo_pagamento = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices = STATUS_PEDIDO)
    criado_em = models.DateTimeField()
    observacao = models.CharField(max_length = 280, null = True, blank = True)
    finalizado_em = models.DateTimeField(blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='funcionario', blank=True, null=True)
    tipo_pedido = models.CharField(db_column='TIPO_PEDIDO', choices = TIPOS_PEDIDO, max_length=30, blank=True, null=True)
    
    class Meta:
        db_table = 'TB_PEDIDO'


class Produto(models.Model):
    id_produto = models.AutoField(db_column='ID_PRODUTO', primary_key=True)  # Field name made lowercase.
    # id = models.IntegerField()
    nome_produto = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.CharField(max_length=400, blank=True, null=True)
    ativo = models.BooleanField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria', related_name="ingredientes", blank=True, null=True)
    ingredientes = models.ManyToManyField(Ingrediente, blank = True)

    class Meta:
        db_table = 'TB_PRODUTO'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=50)
    email = models.CharField(max_length=255, blank=True, null=True)
    senha = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome_usuario}#{self.id_usuario}"

    class Meta:
        db_table = 'TB_USUARIO'
