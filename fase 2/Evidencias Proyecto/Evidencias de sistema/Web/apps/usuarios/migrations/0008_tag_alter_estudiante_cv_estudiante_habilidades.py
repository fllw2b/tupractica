# Generated by Django 5.1.1 on 2024-11-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_estudiante_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='media/cvs/'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='habilidades',
            field=models.ManyToManyField(blank=True, related_name='estudiantes', to='usuarios.tag'),
        ),
    ]