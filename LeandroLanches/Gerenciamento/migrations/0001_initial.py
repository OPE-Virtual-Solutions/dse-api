# Generated by Django 3.2.6 on 2021-09-07 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbBairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('taxa', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'TB_BAIRRO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ativo', models.BooleanField()),
            ],
            options={
                'db_table': 'TB_CATEGORIA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbEndereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'TB_ENDERECO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbIngrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
            ],
            options={
                'db_table': 'TB_INGREDIENTE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbIngredienteProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'TB_INGREDIENTE_PRODUTO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbItemPedido',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
            ],
            options={
                'db_table': 'TB_ITEM_PEDIDO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_pedido', models.CharField(blank=True, max_length=8, null=True)),
                ('atendimento_presencial', models.BooleanField()),
                ('valor_total', models.FloatField(blank=True, null=True)),
                ('metodo_pagamento', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField()),
                ('finalizado_em', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'TB_PEDIDO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('descricao', models.CharField(blank=True, max_length=400, null=True)),
                ('ativo', models.BooleanField()),
            ],
            options={
                'db_table': 'TB_PRODUTO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbUsuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('senha', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'TB_USUARIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCliente',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Gerenciamento.tbusuario')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'TB_CLIENTE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbFuncionario',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Gerenciamento.tbusuario')),
                ('cargo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'TB_FUNCIONARIO',
                'managed': False,
            },
        ),
    ]