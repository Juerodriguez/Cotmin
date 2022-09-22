# Generated by Django 4.1 on 2022-09-21 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTramites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password_hash', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('dni', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tramites',
            fields=[
                ('number', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('estado', models.BooleanField()),
                ('nota_by_admin', models.TextField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.tipotramites')),
            ],
        ),
    ]