# Generated by Django 3.0.3 on 2020-02-16 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('valor_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_final', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fechado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MeioDePagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=200)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fechado', models.BooleanField(default=False)),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fluxo.Caixa')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fluxo.Mesa')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fluxo.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('meio_de_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fluxo.MeioDePagamento')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fluxo.Mesa')),
            ],
        ),
    ]
