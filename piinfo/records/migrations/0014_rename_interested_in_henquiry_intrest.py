# Generated by Django 5.0.1 on 2024-01-22 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_alter_header_table_alter_modules_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='henquiry',
            old_name='interested_in',
            new_name='intrest',
        ),
    ]