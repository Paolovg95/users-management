# Generated by Django 5.0.4 on 2024-04-22 03:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_empresa_direccion_alter_empresa_web_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licitanteprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
