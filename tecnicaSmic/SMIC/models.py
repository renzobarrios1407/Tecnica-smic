from __future__ import unicode_literals

from django.db import models

class Experto(models.Model):
    """experto encargado de estar en el proyecto"""
    codigo = models.IntegerField(default=0, blank=True, null=False,primary_key=True)
    nombre = models.CharField(max_length=25,blank= True, null=True)
    apellido = models.CharField(max_length=25,blank= True, null=True)
    numero_grupo = models.IntegerField(default=0, blank=True, null=True)
    nivel_influencia = models.IntegerField(default=0, blank=True, null=True)
    """llaves foraneas"""
    IDCalificacion = models.ForeignKey('CalificacionSimple',default=0)
    IDCalificacion_Compuesta = models.ForeignKey('CalificacionCompuesta',default=0)
    IDCalificacion_negativa = models.ForeignKey('CalificacionNegativa',default=0)
    IDCalificacion_Escenario_apuesta = models.ForeignKey('Calificacion_Escenario_Apuesta',default=0)
    IDEscenario_apuesta = models.ForeignKey('EscenarioApuesta',default=0)


    def __unicode__(self):
        return self.codigo

class AsociacionExperto(models.Model):
    """clase para asociar muchos expertos a proyectos"""
    codigoID = models.IntegerField(default=0, blank=True, null=False)
    proyectoID = models.IntegerField(default=0, blank=True, null=False,primary_key=True)

    def __unicode__(self):
        return self.codigoID

class Proyecto(models.Model):
    """es el documento que se realiza para la tecnica smic"""
    proyectoID = models.IntegerField(default=0,null=False,primary_key=True)
    nombre = models.CharField(max_length=40,blank= True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    """llaves foraneas"""
    IDDirector = models.ForeignKey('Director',default=0)
    IDEscenario = models.ForeignKey('EscenarioBase',default=0)
    IDEscenario_apuesta = models.ForeignKey('EscenarioApuesta',default=0)
    def __unicode__(self):
        return self.proyectoID

class Director(models.Model):
    """es el lider del proyecto que dirige todo"""
    IDDirector = models.IntegerField(default=0, null=False,primary_key=True)
    nombre = models.CharField(max_length=40,blank=True,null=True)
    apellido = models.CharField(max_length=40,blank=True,null=True)
    """llaves foraneas"""
    IDEscenario = models.ForeignKey('EscenarioBase',default=0)
    IDEscenario_apuesta = models.ForeignKey('EscenarioApuesta',default=0)


    def __unicode__(self):
        return self.IDDirector

class EscenarioBase(models.Model):
    """Clase para crearlas hipotesis del proyecto"""
    IDEscenario = models.IntegerField(default=0,null=False,primary_key=True)
    Nombre_largo = models.CharField(max_length=50,blank=True,null=True)
    Nombre_corto = models.CharField(max_length=15,blank=True,null=True)
    Descripcion = models.TextField(max_length=100,blank=True,null=True)
    """llaves foraneas"""
    IDCalificacion = models.ForeignKey('CalificacionSimple',default=0)
    IDCalificacion_Compuesta = models.ForeignKey('CalificacionCompuesta',default=0)
    IDCalificacion_negativa = models.ForeignKey('CalificacionNegativa',default=0)
    def __unicode__(self):
        return self.IDEscenario

class CalificacionSimple(models.Model):
    """Calificacion de un solo escenario"""
    IDCalificacion = models.IntegerField(default=0, null=False, primary_key=True)
    Calificacion = models.DecimalField(max_digits='10', decimal_places='3')
    Revisado = models.BooleanField(default='False')
    comentarios = models.TextField(default='some text')
    def __unicode__(self):
        return self.IDcalificacion

class CalificacionCompuesta(models.Model):
    """Calificacion de la combinacion de 2 hipotesis simples"""
    IDCalificacion_Compuesta = models.IntegerField(default=0, null=False,primary_key=True)
    Calificacion = models.DecimalField(max_digits='10', decimal_places='3', default='0.0')
    revisado = models.BooleanField(default='False')
    """llaves foraneas"""
    Escenario_Com_1 = models.ForeignKey('EscenarioBase', default=0, related_name='%(class)s_escenario_com_1')
    Escenario_Com_2 = models.ForeignKey('EscenarioBase', default=0, related_name='%(class)s_escenario_com_2')
    def __unicode__(self):
        return self.IDCalificacion_Compuesta

class CalificacionNegativa(models.Model):
    """Calificacion negativa de 2 hipotesis simples"""
    IDCalificacion_negativa = models.IntegerField(default=0,null=False,primary_key=True)
    Calificacion = models.DecimalField(max_digits='10',decimal_places='3',default='0.0')
    """ llaves foraneas"""
    Escenario_neg_1 = models.ForeignKey('EscenarioBase', default=0, related_name='%(class)s_escenario_neg_1')
    Escenario_neg_2 = models.ForeignKey('EscenarioBase', default=0, related_name='%(class)s_escenario_neg_2')

    def __unicode__(self):
        return self.IDCalificacion_negativa

class Calificacion_Escenario_Apuesta(models.Model):
    """Calificacion del escenario apuesta de cada persona"""
    IDCalificacion_Escenario_apuesta = models.IntegerField(default=0, null=False,primary_key=True)
    Causas_Escenario = models.TextField(default='some text')
    consecuencias_Escenario = models.TextField(default='some text')
    """ llaves foraneas """
    IDEscenario = models.ForeignKey('EscenarioBase',default=0)

    def __unicode__(self):
        return self.IDCalificacion_Escenario_apuesta

class EscenarioApuesta(models.Model):
            """Escenario apuesta seleccionado por el experto"""
            IDEscenario_apuesta = models.IntegerField(default=0,null=False,primary_key=True)

            """ llaves foraneas """
            IDCalificacion_Escenario_apuesta = models.ForeignKey('Calificacion_Escenario_Apuesta',default=0)
            IDEscenario = models.ForeignKey('EscenarioBase',default=0)


            def __unicode__(self):
                return self.IDEscenario_apuesta

# Create your models here.