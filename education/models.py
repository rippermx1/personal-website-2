from django.db import models

# Create your models here.
class Education(models.Model):
    career = models.CharField(verbose_name='Carrera', max_length=150)
    university = models.CharField(verbose_name='Universidad', max_length=150)
    description = models.TextField(verbose_name='Descripción')
    start_date = models.DateField(verbose_name='Fecha de inicio')
    end_date = models.DateField(verbose_name='Fecha de término')
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = 'Educación'
        verbose_name_plural = 'Educación'
        ordering = ['-created']

    def __str__(self):
        return self.career