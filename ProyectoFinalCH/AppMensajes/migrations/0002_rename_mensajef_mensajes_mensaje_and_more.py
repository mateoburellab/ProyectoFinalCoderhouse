# Generated by Django 4.1 on 2022-09-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMensajes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajes',
            old_name='mensajef',
            new_name='mensaje',
        ),
        migrations.AddField(
            model_name='mensajes',
            name='fecha_envio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]