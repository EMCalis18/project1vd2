from django.db import models

# Create your models here.

class Departamento(models.Model): #Model es para especificar que vamos a usar a org de django
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado',default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Ares de trabajo'
        ordering = ['name'] #letra abc
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + '-' +self.name + '-' + self.shor_name

