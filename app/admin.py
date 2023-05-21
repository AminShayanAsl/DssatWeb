from django.contrib import admin
from .models import *


class Dssat_cpAdmin(admin.ModelAdmin):
  list_display = ('user' ,'tmax' ,'tmin' ,'rain' ,'srad' ,'rhum' ,'date' ,'hdate' ,'plant' ,'soil' ,'DAP' ,'LAID' ,'GSTD' ,'SWAD' ,'LWAD' ,'GWAD' ,'GAD' ,'GWGD' ,'HIAD' ,'CWAD')
  
admin.site.register(Dssat_cp, Dssat_cpAdmin)
