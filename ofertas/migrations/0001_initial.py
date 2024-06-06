# Generated by Django 5.0.4 on 2024-04-26 22:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('licitaciones', '0004_alter_licitacion_owner'),
        ('users', '0003_alter_licitanteprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.empresa')),
                ('licitacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='licitaciones.licitacion')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OfertaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ofertas.oferta')),
            ],
        ),
    ]
