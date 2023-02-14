from django.contrib import admin
from .models import Institucion,Estudiante,Profesor,Curso,Periodo,Asignatura

# Register your models here.

@admin.register(Institucion)
class NivelAdmin(admin.ModelAdmin):
    list_filter = ('preescolar','primaria','secundaria', 'media','meida_tecnica')

    fieldsets = (
        ('Datos institucionales',{'fields': ('nit','name','Inscription_DANE','codigo_ICFES',
        'telefono1','telefono2')}),
        ('Sedes',{'fields':('sedeA','sedeB')}),
        ('Niveles',{'fields': ('preescolar','primaria','secundaria', 'media','meida_tecnica')}),
        ('Información web',{'fields':('email','web')})
    )

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Periodo)
admin.site.register(Asignatura)


