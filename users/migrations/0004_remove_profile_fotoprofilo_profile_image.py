# Generated by Django 5.0.4 on 2024-05-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_foto_profilo_profile_fotoprofilo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fotoprofilo',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
