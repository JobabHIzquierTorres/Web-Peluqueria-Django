from django.db import models

# Create your models here.


class Info(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    description = models.CharField(max_length=100, verbose_name='Descripción')
    img = models.ImageField(upload_to='prices', verbose_name='Imagen')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Información'


class Prices(models.Model):
    service = models.CharField(max_length=50, verbose_name='Servicio')
    price = models.IntegerField(default=15, verbose_name='Precio')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizado el'
    )

    def __str__(self):
        return str(self.service)

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'
        ordering = ['service']
