# Generated by Django 4.1 on 2022-09-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogs', '0002_alter_blog_fecha_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha_posteo',
            field=models.DateField(blank=True),
        ),
    ]