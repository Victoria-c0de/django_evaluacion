# Generated by Django 4.2.5 on 2023-12-03 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0005_alter_reserva_estado_alter_reserva_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='observacion',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
