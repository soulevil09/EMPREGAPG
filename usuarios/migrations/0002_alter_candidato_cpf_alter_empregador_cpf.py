# Generated by Django 5.1 on 2024-11-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empregador',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
    ]