# Generated by Django 2.2.5 on 2019-10-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20191025_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='cep',
            field=models.CharField(blank='True', max_length=20),
        ),
    ]
