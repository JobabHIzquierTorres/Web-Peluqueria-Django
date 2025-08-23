from django.db import models

# Create your models here.


class Links(models.Model):
    key = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Nombre Clave'
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )
    url = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Enlace'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizado el'
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['name']
