# Generated by Django 5.1.1 on 2024-10-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuPractica', '0002_alter_carrera_id_alter_carrera_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
    ]