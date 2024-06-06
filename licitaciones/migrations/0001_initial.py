# Generated by Django 5.0.4 on 2024-04-22 03:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_alter_licitanteprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Licitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('obs', models.TextField(max_length=300)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.empresa')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'licitacion',
                'verbose_name_plural': 'licitaciones',
            },
        ),
        migrations.CreateModel(
            name='LicitacionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('licitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licitaciones.licitacion')),
            ],
        ),
    ]