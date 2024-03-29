# Generated by Django 4.2.6 on 2023-10-16 10:46

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chandigarh_web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_this_page', models.CharField(max_length=200)),
                ('page_description', tinymce.models.HTMLField()),
                ('website_domain_link', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Class_ikart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_this_page', models.CharField(max_length=200)),
                ('page_description', tinymce.models.HTMLField()),
                ('website_domain_link', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Elive_today',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_this_page', models.CharField(max_length=200)),
                ('page_description', tinymce.models.HTMLField()),
                ('website_domain_link', models.CharField(max_length=150)),
            ],
        ),
    ]
