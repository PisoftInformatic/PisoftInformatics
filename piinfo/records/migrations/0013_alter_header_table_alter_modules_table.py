# Generated by Django 5.0.1 on 2024-01-16 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_demo_data_header'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='header',
            table='header',
        ),
        migrations.AlterModelTable(
            name='modules',
            table='modules',
        ),
    ]