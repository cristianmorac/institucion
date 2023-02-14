from django.db import models
from .choices import TIPO as T, TI, RH, A_MAS, JORNADA as J, M, PERIODO as P, P1

class Institucion(models.Model):
    NIT = models.PositiveBigIntegerField(unique=True)
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

    """ Guardar imagenes
    https://www.youtube.com/watch?v=MAuHTqROt8w
     """

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'
        db_table = 'institucion'
        ordering = ['name'] 
    
    def __str__(self):
        return self.name
    
class Persona(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    tipo_documento = models.CharField(max_length=2,choices=T,default= TI)
    documento = models.PositiveBigIntegerField()
    rh = models.CharField(max_length=8,choices=RH ,default=A_MAS,verbose_name='RH')
    email = models.EmailField(max_length=256, unique=True)
    direccion = models.CharField(max_length=100)    

    class Meta:
        abstract = True

class Profesor(Persona):
    Titulo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        db_table = 'profesor'
        ordering = ['name'] 
    
    def __str__(self):
        return self.name

class Curso(models.Model):
    name = models.CharField(max_length=6, default='')
    jornada = models.CharField(max_length=1,choices=J, default=M)
    director = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        db_table = 'curso'
        ordering = ['name'] 
    
    def __str__(self):
        return self.name

class Estudiante(Persona):
    padre = models.CharField(max_length=50,verbose_name='Padre', blank=True,null=True)
    madre = models.CharField(max_length=50,verbose_name='Madre', blank=True,null=True)
    acudiente = models.CharField(max_length=50,verbose_name='Acudiente')
    fecha_nacimiento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        db_table = 'estudiante'
        ordering = ['name'] 
    
    def __str__(self):
        return self.name

class Asignatura(models.Model):
    name = models.CharField(max_length=50, unique=True)
    profesor = models.ManyToManyField(Estudiante)
    estudiante = models.ManyToManyField(Profesor)

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        db_table = 'asignatura'
        ordering = ['name'] 
    
    def __str__(self):
        return self.name

class ModeloNotas(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ManyToManyField(Curso)
    nota1 = models.DecimalField()
    nota2 = models.DecimalField()
    nota3 = models.DecimalField()
    nota4 = models.DecimalField()
    nota5 = models.DecimalField()

    class Meta:
        abstract = True

class Periodo(ModeloNotas):
    name = models.CharField(max_length=2,choices=P, default=P1)

