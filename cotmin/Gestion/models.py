from django.db import models

# Create your models here.


class Tramites(models.Model):
    """llave foranea a Tipo de tramites, si elimino un tipo de tramite se eliminaran todos los tramites vinculados"""
    number = models.PositiveIntegerField(primary_key=True, unique=True)
    date = models.DateField()
    tipo = models.ForeignKey('TipoTramites', null=False, blank=False, on_delete=models.CASCADE)
    estado = models.BooleanField()
    nota_by_admin = models.TextField()

    def __str__(self):
        txt = "Tramite N°: {0}, Año: {1}"
        return txt.format(self.number, self.date)


class TipoTramites(models.Model):
    tipo = models.CharField(max_length=255)

    def __str__(self):
        txt = "Tipo de Tramite: {0}"
        return txt.format(self.tipo)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique=True, null=False, blank=False)
    password_hash = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dni = models.PositiveIntegerField()

    def datos_de_usuario(self):
        txt = "Nombre Completo:{0} {1}, DNI:{2}"
        return txt.format(self.name, self.surname, self.dni)