from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    description = models.CharField(max_length=100, verbose_name='Descripción')
    price = models.IntegerField(default=15, verbose_name='Precio')
    img = models.ImageField(upload_to='services', verbose_name='Imagen')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['title']
