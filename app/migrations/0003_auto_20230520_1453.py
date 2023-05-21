# Generated by Django 3.2.18 on 2023-05-20 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20230519_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dssat_cp',
            name='SOIL',
        ),
        migrations.RemoveField(
            model_name='dssat_cp',
            name='prec',
        ),
        migrations.RemoveField(
            model_name='dssat_cp',
            name='rad',
        ),
        migrations.RemoveField(
            model_name='dssat_cp',
            name='rh',
        ),
        migrations.RemoveField(
            model_name='dssat_cp',
            name='tn',
        ),
        migrations.AddField(
            model_name='dssat_cp',
            name='hdate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='dssat_cp',
            name='rain',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dssat_cp',
            name='rhum',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dssat_cp',
            name='soil',
            field=models.CharField(blank=True, choices=[('SIL', 'SIL'), ('SI', 'SI'), ('SL', 'SL'), ('SIC', 'SIC'), ('SCL', 'SCL'), ('L', 'L'), ('C', 'C'), ('SICL', 'SICL'), ('LS', 'LS'), ('SC', 'SC'), ('CL', 'CL'), ('S', 'S')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='dssat_cp',
            name='srad',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dssat_cp',
            name='tmax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dssat_cp',
            name='tmin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='CWAD',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='DAP',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='GAD',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='GSTD',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='GWAD',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='GWGD',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='HIAD',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='LAID',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='LWAD',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='SWAD',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='plant',
            field=models.CharField(blank=True, choices=[('Maize', 'Maize'), ('Millet', 'Millet'), ('Sugarbeet', 'Sugarbeet'), ('Rice', 'Rice'), ('Soybean', 'Soybean'), ('Sunflower', 'Sunflower')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='dssat_cp',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]