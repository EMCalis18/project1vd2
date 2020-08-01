from django.contrib import admin
from .models import Empleado, habilidad 
# Register your models here.

admin.site.register(habilidad)


class EmpledoAdmin(admin.ModelAdmin):
 
    list_display = ( #para listarlos en tablas
        'Nombre_completo',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'id',
    )
 
    def Nombre_completo(self, obj):#funcion para que me muestre todo el nombre
        #toda la operacion
        
        return obj.first_name + ' ' + obj.last_name
 
    search_fields = ('first_name',) #para poner un buscador 
    list_filter = ('job', 'habilidad',)#para poner un filtro
    filter_horizontal = ('habilidad',)#solo funcionas en entidades de muchos a muchos


admin.site.register(Empleado,EmpledoAdmin)