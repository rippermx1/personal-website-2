# Generated by Django 2.1.5 on 2020-04-23 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['-created'], 'verbose_name': 'Habilidad', 'verbose_name_plural': 'Habilidades'},
        ),
        migrations.AddField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='skill',
            name='domain',
            field=models.IntegerField(default=0, null=True, verbose_name='Dominio'),
        ),
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='skill',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de actualuzación'),
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='skills.SkillCategory', verbose_name='Categoría'),
        ),
    ]
