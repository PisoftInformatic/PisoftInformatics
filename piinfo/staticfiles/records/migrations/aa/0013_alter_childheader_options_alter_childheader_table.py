# Generated by Django 4.2.7 on 2023-11-24 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_childheader_delete_childheaders'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='childheader',
            options={'ordering': ['priority'], 'verbose_name_plural': 'childHeader'},
        ),
        migrations.AlterModelTable(
            name='childheader',
            table='childHeader',
        ),
    ]
