from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Importa tus otros modelos (ajusta el nombre de las rutas si es distinto)
from .mesero import Mesero
from .cliente import Cliente
from .mesa import Mesa
from .plato import Plato


class Orden(models.Model):
    ESTADOS = [
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    ]

    mesero = models.ForeignKey(Mesero, on_delete=models.SET_NULL, null=True, blank=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT)
    platos = models.ManyToManyField(Plato, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='abierto')
    fechaHora = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        super().clean()
        if self.estado == 'abierto':
            qs = Orden.objects.filter(mesa=self.mesa, estado='abierto')
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                raise ValidationError("Ya existe una orden abierta para esta mesa.")

        if self.estado == 'abierto' and self.cliente is not None:
            raise ValidationError("El cliente se asigna solo cuando se cierra/paga la orden.")

    def __str__(self):
        return f"Orden #{self.id} - {self.get_estado_display()}"
