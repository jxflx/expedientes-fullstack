from django.db import models

class Doctor(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    primerApellido = models.CharField(max_length=25, blank=True)
    segundoApellido = models.CharField(max_length=25, blank=True)

    def __str__(self):
        nombreCompleto = self.primerApellido + " " + self.segundoApellido + " " + self.nombre
        return nombreCompleto


class Paciente(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    primerApellido = models.CharField(max_length=25, blank=True)
    segundoApellido = models.CharField(max_length=25, blank=True)
    # sexos disponibles
    sexosDisponibles = {
        "F": "Femenino",
        "M": "Masculino"
    }
    sexo = models.CharField(max_length=1, choices=sexosDisponibles)
    curp = models.CharField(max_length=18)
    fechaNacimiento = models.DateField(blank=True)
    expediente = models.CharField(max_length=100, blank=True)

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='pacientes')

    def __str__(self):
        nombreCompleto = self.primerApellido + " " + self.segundoApellido + " " + self.nombre
        return nombreCompleto

class Consulta(models.Model):
    edad = models.IntegerField(blank=True)
    fecha = models.DateField(blank=True)
    fechaProximaCita = models.DateField(blank=True)
    peso = models.DecimalField(max_digits=3, decimal_places=3 ,blank=True)
    talla = models.DecimalField(max_digits=3, decimal_places=3 ,blank=True)
    imc = models.IntegerField(blank=True)
    circunferenciaCintura = models.DecimalField(max_digits=3, decimal_places=3 ,blank=True)
    presionSistolica = models.IntegerField(blank=True)
    presionDiastolica = models.IntegerField(blank=True)
    frecuenciaCardiaca = models.IntegerField(blank=True)
    frecuenciaRespiratoria = models.IntegerField(blank=True)
    temperatura = models.DecimalField(max_digits=3, decimal_places=3 ,blank=True)
    saturacionOxigeno = models.IntegerField(blank=True)
    glucemia = models.IntegerField(blank=True)
    dx1 = models.CharField(max_length=100, blank=True)
    dx2 = models.CharField(max_length=100, blank=True)
    dx3 = models.CharField(max_length=100, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')






# Create your models here.
