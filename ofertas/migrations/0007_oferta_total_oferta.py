# Generated by Django 5.0.6 on 2024-06-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0006_alter_ofertaitem_licitacion_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='total_oferta',
            field=models.IntegerField(null=True),
        ),
    ]