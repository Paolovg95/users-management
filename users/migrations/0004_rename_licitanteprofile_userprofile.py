# Generated by Django 5.0.4 on 2024-04-28 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_licitanteprofile_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LicitanteProfile',
            new_name='UserProfile',
        ),
    ]