# Generated by Django 4.2.6 on 2023-10-24 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bossapp', '0023_delete_website_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Desktop_Applications',
        ),
        migrations.DeleteModel(
            name='Mobile_Applications',
        ),
        migrations.DeleteModel(
            name='Web_Applications',
        ),
    ]
