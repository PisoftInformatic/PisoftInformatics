# Generated by Django 3.2.21 on 2023-09-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bossapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career_With_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=30)),
                ('sub_title', models.CharField(max_length=30)),
                ('job_description', models.TextField()),
                ('experience_required', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
    ]
