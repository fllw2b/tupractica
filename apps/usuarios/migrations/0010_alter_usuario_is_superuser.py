# Generated by Django 5.1.1 on 2024-11-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_estudiante_habilidades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]