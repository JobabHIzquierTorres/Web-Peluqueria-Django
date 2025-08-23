from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=50, verbose_name='título')
    description = models.CharField(max_length=100, verbose_name='Descripción')
    content = models.TextField(verbose_name='Contenido')
    since = models.CharField(max_length=50, verbose_name='Desde')
    since_description = models.CharField(
        max_length=100, verbose_name='Desde_Descripción')
    clients = models.CharField(
        max_length=50, verbose_name='Número de Clientes')
    clients_description = models.CharField(
        max_length=100, verbose_name='Clientes_Descripción')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'


class Barbers(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.CharField(max_length=200, verbose_name='Descripción')
    img = models.ImageField(upload_to='Barbers', verbose_name='Foto Empleado')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Barbero'
        verbose_name_plural = 'Barberos'
