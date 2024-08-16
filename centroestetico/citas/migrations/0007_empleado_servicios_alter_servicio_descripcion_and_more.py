# Generated by Django 5.0.8 on 2024-08-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0006_alter_cita_options_alter_cliente_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='servicios',
            field=models.ManyToManyField(related_name='empleados', to='citas.servicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='duracion',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
