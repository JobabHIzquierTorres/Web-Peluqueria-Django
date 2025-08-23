from django.db import models
from about.models import Barbers

# Create your models here.


class Links(models.Model):
    """
      uso de choices
    """

    SOCIAL_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
    ]

    barber = models.ForeignKey(
        Barbers, on_delete=models.CASCADE, related_name='social_links')

    social_networks = models.CharField(
        max_length=20,
        choices=SOCIAL_CHOICES,
        verbose_name='Redes Sociales'
    )

    key = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Palabra Clave'
    )
    name = models.CharField(max_length=200, verbose_name='Nombre')
    url = models.URLField(verbose_name='Enlace')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']
