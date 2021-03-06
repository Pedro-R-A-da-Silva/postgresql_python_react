# Generated by Django 3.2.10 on 2022-06-11 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sede', models.CharField(max_length=500)),
                ('Lotaçao', models.CharField(max_length=500)),
                ('cargo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('matricula', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=500)),
                ('setor', models.CharField(max_length=500)),
                ('ativo', models.BooleanField(default=False)),
                ('foto', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Situação',
            fields=[
                ('operacional', models.BooleanField(default=False, primary_key=True, serialize=False)),
                ('motivo', models.TextField()),
            ],
        ),
    ]
