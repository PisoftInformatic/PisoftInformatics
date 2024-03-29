# Generated by Django 4.2.6 on 2023-10-18 06:38

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Graphic_Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Web_Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Web_Hosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Web_Marketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
    ]
