# Generated by Django 4.1.4 on 2023-03-17 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_cargos_usuario_senha_alter_usuario_nome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cargo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='cargo',
            field=models.ManyToManyField(to='autenticacao.cargos'),
        ),
    ]