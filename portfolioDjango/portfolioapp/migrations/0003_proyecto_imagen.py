# Generated by Django 4.2 on 2023-11-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]
