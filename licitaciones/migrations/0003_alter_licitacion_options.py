# Generated by Django 5.0.4 on 2024-04-26 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licitaciones', '0002_alter_licitacion_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='licitacion',
            options={'permissions': [('can_view_all_licitaciones', 'Can view licitaciones only users that subscribed.')], 'verbose_name': 'licitacion', 'verbose_name_plural': 'licitaciones'},
        ),
    ]