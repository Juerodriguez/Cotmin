from django.db import models
from django.contrib.auth.models import User

ESTADO_TRAMITE = (
        ('P', 'Pendiente'),
        ('R', 'Revisado'),
        ('C', 'En curso'),
    )


class Tramites(models.Model):
    """
    llave foranea a Tipo de tramites, si elimino un tipo de tramite se eliminaran todos los tramites vinculados
    """
    number = models.PositiveIntegerField(primary_key=True, unique=True)
    solicitante = models.CharField(max_length=255, default="Sin datos")
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True)
    completed_by = models.CharField(max_length=255, null=True)
    # file = models.FileField(upload_to='archivos/%Y/%m')
    tipo = models.ForeignKey('TipoTramites', null=False, blank=False, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=ESTADO_TRAMITE, default="P")
    nota_by_admin = models.TextField()
    user = models.ForeignKey(User, models.SET_NULL, null=True)

    def __str__(self):
        txt = "Tramite N°: {0}, Año: {1}"
        return txt.format(self.number, self.date_created)


class TipoTramites(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo
