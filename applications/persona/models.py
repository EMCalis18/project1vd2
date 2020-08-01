from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

#hay que importar la tabla departamento proque se relaciona con esta tabla


# Create your models here.
class habilidad (models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' +self.habilidad    


class Empleado(models.Model):
    """"" MODELO PARA TABLA EMPLEADO"""""
    
    JOB_CHOICES = [
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),

    ]


    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField(
        'Nombre completo',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=30,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField('foto', upload_to='empleado',  blank=True , null=True)
    habilidad = models.ManyToManyField(habilidad)
    hoja_vida = RichTextField()


    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['first_name' , 'last_name'  ]
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' +self.first_name + '-' + self.last_name
