# Generated by Django 4.2.6 on 2023-10-31 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bossapp', '0025_homepage_recent_project_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery Image'},
        ),
        migrations.AlterModelOptions(
            name='homepage_recent_project_data',
            options={'verbose_name': 'Recent Project'},
        ),
    ]
