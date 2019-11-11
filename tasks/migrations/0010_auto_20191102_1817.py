# Generated by Django 2.2.5 on 2019-11-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20191026_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocorrencia',
            name='geolocalidade',
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='cep',
            field=models.CharField(blank='True', max_length=20, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='cidade',
            field=models.CharField(blank='True', max_length=100, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='cpf',
            field=models.CharField(max_length=15, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='endereco',
            field=models.CharField(blank='True', max_length=100, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='telefone',
            field=models.CharField(blank='True', max_length=20, verbose_name='Telefone'),
        ),
    ]
