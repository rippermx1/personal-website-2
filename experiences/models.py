from django.db import models

# Create your models here.
class Experience(models.Model):
    role = models.CharField(verbose_name='Cargo', max_length=150)
    company = models.CharField(verbose_name='Empresa', max_length=150)
    description = models.TextField(verbose_name='Descripción')
    begin_date = models.DateField(verbose_name='Fecha contratación')
    end_date = models.DateField(verbose_name='Fecha término contrato')
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de modificación', auto_now=True)

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
        ordering = ['-created']

    def __str__(self):
        return self.company