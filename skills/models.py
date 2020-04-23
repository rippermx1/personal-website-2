from django.db import models

# Create your models here.
class SkillCategory(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name
    

class Skill(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100, null=True)
    domain = models.IntegerField(verbose_name='Dominio', default=0, blank=False, null=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.DO_NOTHING, verbose_name='Categoría', null=True)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now=True, null=True)
    updated = models.DateTimeField(verbose_name='Fecha de actualuzación', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['-created']

    def __str__(self):
        return self.name