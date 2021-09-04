# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbBairro(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    taxa = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BAIRRO'

    def __str__(self):
        return f"{self.uf} - {self.nome}"


class TbCliente(models.Model):
    id = models.OneToOneField('TbUsuario', models.DO_NOTHING, db_column='id', primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CLIENTE'
        unique_together = (('id', 'id'),)

    def __str__(self):
        return f"{self.nome}"


class TbEndereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.ForeignKey(TbBairro, models.DO_NOTHING, db_column='bairro', blank=True, null=True)
    cliente = models.ForeignKey(TbCliente, models.DO_NOTHING, db_column='cliente')

    class Meta:
        managed = False
        db_table = 'TB_ENDERECO'

    def __str__(self):
        return f"{self.cep} - {self.logradouro}"


class TbFuncionario(models.Model):
    id = models.OneToOneField('TbUsuario', models.DO_NOTHING, db_column='id', primary_key=True)
    cargo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'TB_FUNCIONARIO'

    def __str__(self):
        return f"{self.id}"


class TbIngrediente(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TB_INGREDIENTE'

    def __str__(self): 
        return f"{self.nome}"


class TbProduto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.CharField(max_length=400, blank=True, null=True)
    ativo = models.BooleanField()
    categoria = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_PRODUTO'

    def __str__(self): 
        return f"{self.nome}"

class TbIngredienteProduto(models.Model):
    produto = models.ForeignKey(TbProduto, models.DO_NOTHING, db_column='produto')
    ingrediente = models.ForeignKey(TbIngrediente, models.DO_NOTHING, db_column='ingrediente')

    class Meta:
        managed = False
        db_table = 'TB_INGREDIENTE_PRODUTO'
        unique_together = (('produto', 'ingrediente', 'ingrediente'),)
    
    def __str__(self): 
        return f"{self.produto} {self.ingrediente}"


class TbItemPedido(models.Model):
    id = models.IntegerField(primary_key=True)
    produto = models.ForeignKey('TbProduto', models.DO_NOTHING, db_column='produto')
    pedido = models.ForeignKey('TbPedido', models.DO_NOTHING, db_column='pedido', blank=True, null=True)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    class Meta:
        managed = False
        db_table = 'TB_ITEM_PEDIDO'
    
    def __str__(self): 
        return f"{self.pedido} {self.produto}"


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
        managed = False
        db_table = 'TB_PEDIDO'



class TbUsuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=255, blank=True, null=True)
    senha = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'TB_USUARIO'

    def __str__(self): 
        return f"{self.nome}"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
