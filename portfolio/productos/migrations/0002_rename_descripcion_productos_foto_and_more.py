# Generated by Django 4.0.5 on 2022-07-13 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='descripcion',
            new_name='foto',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='correoProveedor',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='fechaIncorporacion',
        ),
    ]