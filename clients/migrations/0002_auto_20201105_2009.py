# Generated by Django 3.1.3 on 2020-11-06 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='refence',
            new_name='reference',
        ),
    ]
