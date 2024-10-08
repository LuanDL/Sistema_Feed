# Generated by Django 3.2.25 on 2024-04-27 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9)),
                ('endereco', models.CharField(max_length=50)),
                ('numero', models.CharField(default='0', max_length=5)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=14)),
                ('grupoacesso', models.CharField(choices=[('importacao', 'Importação'), ('usuario', 'Usuário'), ('administrador', 'Administrador')], default='importacao', max_length=50)),
                ('observacoes', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
