# Generated by Django 5.1.1 on 2024-11-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_remove_anunciopractica_direccion_and_more'),
        ('usuarios', '0008_tag_alter_estudiante_cv_estudiante_habilidades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anunciopractica',
            name='requisitos',
        ),
        migrations.AddField(
            model_name='anunciopractica',
            name='requisitos',
            field=models.ManyToManyField(blank=True, related_name='anuncios_practica', to='usuarios.tag'),
        ),
    ]
