# Generated by Django 4.2.3 on 2023-10-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ERP_Solutions_Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_page_heading', models.TextField(max_length=300)),
                ('education_page_description', models.TextField()),
                ('finance_page_heading', models.TextField()),
                ('medical_page_heading', models.TextField(max_length=300)),
                ('medical_page_description', models.TextField()),
                ('automobile_page_heading', models.TextField(max_length=300)),
                ('automobile_page_description', models.TextField()),
                ('tours_page_heading', models.TextField(max_length=300)),
                ('tours_page_description', models.TextField()),
                ('services_page_heading', models.TextField(max_length=300)),
                ('services_page_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('page_description', models.CharField(max_length=200)),
                ('card_title', models.CharField(max_length=100)),
                ('card_description', models.CharField(max_length=200)),
            ],
        ),
    ]
