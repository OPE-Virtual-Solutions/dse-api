from django.db import models


class TbBairro(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    taxa = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'TB_BAIRRO'


class TbCategoria(models.Model):
    nome = models.CharField(max_length=50)
    ativo = models.BooleanField()

    class Meta:
        db_table = 'TB_CATEGORIA'


class TbCliente(models.Model):
    id = models.OneToOneField('TbUsuario', models.DO_NOTHING, db_column='id', primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'TB_CLIENTE'


class TbEndereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.ForeignKey(TbBairro, models.DO_NOTHING, db_column='bairro', blank=True, null=True)
    cliente = models.ForeignKey(TbCliente, models.DO_NOTHING, db_column='cliente')

    class Meta:
        db_table = 'TB_ENDERECO'


class TbFuncionario(models.Model):
    id = models.OneToOneField('TbUsuario', models.DO_NOTHING, db_column='id', primary_key=True)
    cargo = models.CharField(max_length=255)

    class Meta:
        db_table = 'TB_FUNCIONARIO'


class TbIngrediente(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    class Meta:
        db_table = 'TB_INGREDIENTE'


class TbProduto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.CharField(max_length=400, blank=True, null=True)
    ativo = models.BooleanField()
    quantidade = models.BigIntegerField(default = 0)
    categoria = models.ForeignKey(TbCategoria, models.DO_NOTHING, db_column='categoria', blank=True, null=True)

    class Meta:
        db_table = 'TB_PRODUTO'


class TbIngredienteProduto(models.Model):
    produto = models.ForeignKey(TbProduto, models.DO_NOTHING, db_column='produto', related_name="ingredientes")
    ingrediente = models.ForeignKey(TbIngrediente, models.DO_NOTHING, db_column='ingrediente', related_name="produtos")

    class Meta:
        db_table = 'TB_INGREDIENTE_PRODUTO'


class TbItemPedido(models.Model):
    produto = models.ForeignKey('TbProduto', models.DO_NOTHING, db_column='produto')
    pedido = models.ForeignKey('TbPedido', models.DO_NOTHING, db_column='pedido', blank=True, null=True)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    class Meta:
        db_table = 'TB_ITEM_PEDIDO'


class TbPedido(models.Model):
    codigo_pedido = models.CharField(max_length=8, blank=True, null=True)
    cliente = models.ForeignKey(TbCliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    endereco = models.ForeignKey(TbEndereco, models.DO_NOTHING, db_column='endereco', blank=True, null=True)
    atendimento_presencial = models.BooleanField()
    valor_total = models.FloatField(blank=True, null=True)
    metodo_pagamento = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    criado_em = models.DateTimeField()
    finalizado_em = models.DateTimeField(blank=True, null=True)
    funcionario = models.ForeignKey(TbFuncionario, models.DO_NOTHING, db_column='funcionario', blank=True, null=True)

    class Meta:
        db_table = 'TB_PEDIDO'


class TbUsuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=255, blank=True, null=True)
    senha = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255)

    class Meta:
        db_table = 'TB_USUARIO'
