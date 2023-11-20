# Generated by Django 4.2.3 on 2023-09-22 06:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('bossapp', '0003_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech_Descovery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
    ]
