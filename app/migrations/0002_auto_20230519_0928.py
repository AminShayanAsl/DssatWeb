# Generated by Django 3.2.18 on 2023-05-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dssat_cp',
            name='SOIL',
            field=models.CharField(choices=[('SL', 'SL'), ('LS', 'LS'), ('L', 'L'), ('S', 'S'), ('SC', 'SC'), ('SIL', 'SIL'), ('SI', 'SI'), ('CL', 'CL'), ('SCL', 'SCL'), ('C', 'C'), ('SICL', 'SICL'), ('SIC', 'SIC')], max_length=15),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]