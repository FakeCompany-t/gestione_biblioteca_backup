# Generated by Django 5.0.4 on 2024-05-15 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0007_libro_copertina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autori',
        ),
    ]
