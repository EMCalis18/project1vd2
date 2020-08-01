from django.db import models

# Create your models here.

class Pruebabase(models.Model):
    titulo = models.CharField( max_length=50)
    subtitulo = models.CharField( max_length=50)
    cantidad = models.IntegerField()


    def _str_(self):
        return self.titulo