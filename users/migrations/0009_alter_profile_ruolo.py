# Generated by Django 5.0.4 on 2024-05-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ruolo',
            field=models.CharField(choices=[('studente', 'Studente'), ('docente', 'Docente'), ('bibliotecario', 'Bibliotecario'), ('segreteria', 'Segreteria'), ('gestore_comodato', "Gestore Comodato d'Uso"), ('amministratore', 'Amministratore')], max_length=20),
        ),
    ]