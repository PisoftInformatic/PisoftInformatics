# Generated by Django 4.2.6 on 2023-10-20 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_alter_registration_caddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='henquiry',
            old_name='collage',
            new_name='college',
        ),
    ]
