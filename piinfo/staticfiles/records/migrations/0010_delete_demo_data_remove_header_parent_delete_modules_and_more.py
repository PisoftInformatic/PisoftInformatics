# Generated by Django 5.0.1 on 2024-01-16 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_demo_data_modules_users_alter_apply_job_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Demo_Data',
        ),
        migrations.RemoveField(
            model_name='header',
            name='parent',
        ),
        migrations.DeleteModel(
            name='modules',
        ),
        migrations.DeleteModel(
            name='Header',
        ),
    ]
