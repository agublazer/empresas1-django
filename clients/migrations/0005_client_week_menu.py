# Generated by Django 3.1.3 on 2020-11-13 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('clients', '0004_auto_20201105_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='week_menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.weekmenu'),
        ),
    ]
