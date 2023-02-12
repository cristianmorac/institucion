from django.db import models

# Create your models here.

PREESCOLAR = 'K'
PRIMARIA = 'P'
SECUNDARIA = 'S'
MEDIA = 'M'

class Institucion(models.Model):
    nit = models.PositiveBigIntegerField(unique=True)
    name = models.CharField(max_length=256, verbose_name='Institución')
    preescolar = models.BooleanField('Preescolar',default=False)
    primaria = models.BooleanField('Primaria',default=False)
    secundaria = models.BooleanField('secundaria',default=False)
    media = models.BooleanField('Media',default=False)
    meida_tecnica = models.BooleanField('Media técnica',default=False)
    Inscription_DANE = models.PositiveBigIntegerField()
    codigo_ICFES = models.PositiveBigIntegerField()
    sedeA = models.CharField(max_length=50, verbose_name='Sede A', blank=True, null=True,unique=True)
    sedeB = models.CharField(max_length=50, verbose_name='Sede B', blank=True, null=True,unique=True)
    telefono1 = models.PositiveBigIntegerField(blank=True, null=True,unique=True)
    telefono2 = models.PositiveBigIntegerField(blank=True, null=True,unique=True)
    email = models.EmailField(max_length=256,unique=True)
    web = models.URLField(max_length=256, verbose_name='página web')

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'
        db_table = 'institucion'
        ordering = ['name'] 
    
    def __str__(self):
        return self.name
    
