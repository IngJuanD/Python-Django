from django.db import models
from django.forms import ImageField


# Create your models here.

opciones = [

    [0,"CEDULA CIUDADANIA"],
    [1,"CEDULA EXTRANGERIA"],
    [2,"PASAPORTE"]
]

class Cliente(models.Model):
    identificacion_cl=models.CharField(primary_key=True,max_length=12,verbose_name="Identificación")
    tipo_id_cl=models.IntegerField(choices=opciones,verbose_name="Tipo Identificación")
    nombre_cl=models.CharField(max_length=22,verbose_name="Nombres")
    apellido_cl=models.CharField(max_length=25,verbose_name="Apellidos")
    correo_cl=models.EmailField(verbose_name="Correo Electrónico")
    telefono_cl=models.CharField(max_length=14,verbose_name="Teléfono")

    def __str__(self):
        return '%s %s %s' %(self.identificacion_cl,self.nombre_cl,self.apellido_cl)


class Plan(models.Model):
    id_plan=models.AutoField(primary_key=True,verbose_name="Plan")
    nombre_plan=models.CharField(max_length=22,verbose_name="Nombre")
    descripcion_plan=models.CharField(max_length=50,verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Costo Dia")

    def __str__(self):
        return '%s %s %s' %(self.id_plan,self.nombre_plan,self.descripcion_plan)


class Habitacion(models.Model):
    id_hb=models.CharField(primary_key=True,max_length=4,verbose_name="Num. Habitacion")
    capacidad=models.PositiveIntegerField(verbose_name="Capacidad")
    descripcion_hb=models.CharField(max_length=50,verbose_name="Descripción")
    id_plan=models.ForeignKey(Plan, verbose_name=("Plan"), on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='habitaciones', null=True,verbose_name="Foto");

    def __str__(self):
        return '%s %s %s' %(self.id_hb,self.capacidad,self.descripcion_hb)

class Reserva(models.Model):
    id_reserva=models.AutoField(primary_key=True,verbose_name="Id. Reserva")
    fecha_inicio=models.DateField(verbose_name="Fecha Inicio")
    fecha_fin=models.DateField(verbose_name="Fecha Fin")
    identificacion_cl=models.ForeignKey(Cliente, verbose_name=("Id. Cliente"), on_delete=models.CASCADE)
    id_hb=models.ForeignKey(Habitacion, verbose_name=("Id Habitacion"), on_delete=models.CASCADE)
    #id_plan=models.ForeignKey(Plan, verbose_name=("Plan"), on_delete=models.CASCADE)


    def __str__(self):
        return '%s %s %s' %(self.id_reserva,self.fecha_inicio,self.identificacion_cl)

opcionesContacto = [
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitación"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField()
    tipo=models.IntegerField(choices=opcionesContacto)
    mensaje=models.TextField()

    def __str__(self):
        return '%s %s %s' %(self.nombre,self.correo,self.tipo)
