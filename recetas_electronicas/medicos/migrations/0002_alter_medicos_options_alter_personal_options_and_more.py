# Generated by Django 4.2.4 on 2023-08-17 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicos',
            options={'ordering': ['nombre'], 'verbose_name': 'Medico', 'verbose_name_plural': 'Medicos'},
        ),
        migrations.AlterModelOptions(
            name='personal',
            options={'ordering': ['nombre'], 'verbose_name': 'Personal', 'verbose_name_plural': 'Personal pero en plural'},
        ),
        migrations.AlterModelOptions(
            name='turnos',
            options={'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
        migrations.AlterField(
            model_name='turnos',
            name='especialidad',
            field=models.CharField(max_length=15),
        ),
    ]
