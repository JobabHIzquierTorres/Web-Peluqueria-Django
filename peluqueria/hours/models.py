from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Info(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.CharField(max_length=100, verbose_name='Descripción')
    img = models.ImageField(upload_to='hours', verbose_name='Imagen')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizado el'
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'


class Hours(models.Model):
    day = models.CharField(max_length=20, verbose_name='Día')
    open = models.TimeField(
        blank=True,
        null=True,
        verbose_name='Hora de apertura'
    )
    close = models.TimeField(
        blank=True,
        null=True,
        verbose_name='Hora de cierre'
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Orden del día'
    )
    is_open = models.BooleanField(default=True, verbose_name='¿Abierto?')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizado el'
    )

    """
      Evitar añadir hora de cierre anterior a la hora de salida
    """

    def clean(self):
        if self.is_open:
            if self.open is None or self.close is None:
                raise ValidationError(
                    "Debes ingresar las horas si el día está marcado como abierto."
                )
            if self.close <= self.open:
                raise ValidationError(
                    "La hora de cierre debe ser posterior a la hora de apertura."
                )
        else:
            # en caso de estar cerrada la pelu
            self.open = None
            self.close = None

    def __str__(self):
        if not self.is_open or not self.open or not self.close:
            return f"{self.day}: Cerrado"
        return f"{self.day}: {self.open.strftime('%I:%M %p')} - {self.close.strftime('%I:%M %p')}"

    class Meta:
        verbose_name = 'Hora'
        verbose_name_plural = 'Horas'
        ordering = ['order']
