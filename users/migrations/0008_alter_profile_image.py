# Generated by Django 5.0.4 on 2024-05-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_default.png', upload_to='profile_pics'),
        ),
    ]