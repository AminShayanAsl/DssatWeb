from django.db import models
from django.contrib.auth.models import User


plant_choices = (
    ('Maize', 'Maize'),
    ('Millet', 'Millet'),
    ('Sugarbeet', 'Sugarbeet'),
    ('Rice', 'Rice'),
    ('Soybean', 'Soybean'),
    ('Sunflower', 'Sunflower'),
)

soil_choices = {
    ('S', 'S'),
    ('LS', 'LS'),  
    ('SL', 'SL'), 
    ('L', 'L'), 
    ('SIL', 'SIL'), 
    ('SI', 'SI'), 
    ('SCL', 'SCL'), 
    ('CL', 'CL'), 
    ('SICL', 'SICL'), 
    ('SC', 'SC'), 
    ('SIC', 'SIC'), 
    ('C', 'C'), 
}

class Dssat_cp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tmax = models.FloatField(null=True, blank=True)
    tmin = models.FloatField(null=True, blank=True)
    rain = models.FloatField(null=True, blank=True)
    srad = models.FloatField(null=True, blank=True)
    rhum = models.FloatField(null=True, blank=True)
    date = models.CharField(max_length=10, null=True, blank=True)
    hdate = models.CharField(max_length=10, null=True, blank=True)
    plant = models.CharField(choices=plant_choices, max_length=15, null=True, blank=True)
    soil = models.CharField(choices=soil_choices, max_length=15, null=True, blank=True)
    DAP = models.FloatField(null=True, blank=True)
    LAID = models.FloatField(null=True, blank=True)
    GSTD = models.FloatField(null=True, blank=True)
    SWAD = models.FloatField(null=True, blank=True)
    LWAD = models.FloatField(null=True, blank=True)
    GWAD = models.FloatField(null=True, blank=True)
    GAD = models.FloatField(null=True, blank=True)
    GWGD = models.FloatField(null=True, blank=True)
    HIAD = models.FloatField(null=True, blank=True)
    CWAD = models.FloatField(null=True, blank=True)
