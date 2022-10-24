# Generated by Django 4.0.4 on 2022-10-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_libro_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='image',
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='libros/', verbose_name='Imagen'),
        ),
    ]
