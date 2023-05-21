# Generated by Django 3.2.18 on 2023-05-18 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dssat_cp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tn', models.FloatField()),
                ('rad', models.FloatField()),
                ('prec', models.FloatField()),
                ('rh', models.FloatField()),
                ('date', models.DateField()),
                ('plant', models.CharField(choices=[('Maize', 'Maize'), ('Millet', 'Millet'), ('Sugarbeet', 'Sugarbeet'), ('Rice', 'Rice'), ('Sorghum', 'Sorghum'), ('Sweetcorn', 'Sweetcorn'), ('Alfalfa', 'Alfalfa'), ('Bermudagrass', 'Bermudagrass'), ('Soybean', 'Soybean'), ('Canola', 'Canola'), ('Sunflower', 'Sunflower'), ('Potato', 'Potato'), ('Tomato', 'Tomato'), ('Cabbage', 'Cabbage')], max_length=15)),
                ('SOIL', models.CharField(choices=[('SIC', 'SIC'), ('SI', 'SI'), ('SCL', 'SCL'), ('SICL', 'SICL'), ('L', 'L'), ('SIL', 'SIL'), ('LS', 'LS'), ('SL', 'SL'), ('S', 'S'), ('C', 'C'), ('SC', 'SC'), ('CL', 'CL')], max_length=15)),
                ('DAP', models.FloatField()),
                ('LAID', models.FloatField()),
                ('GSTD', models.FloatField()),
                ('SWAD', models.FloatField()),
                ('LWAD', models.FloatField()),
                ('GWAD', models.FloatField()),
                ('GAD', models.FloatField()),
                ('GWGD', models.FloatField()),
                ('HIAD', models.FloatField()),
                ('CWAD', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
