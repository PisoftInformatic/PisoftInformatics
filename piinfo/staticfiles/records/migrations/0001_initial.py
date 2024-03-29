# Generated by Django 4.2.6 on 2023-10-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply_Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('position_applied_for', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=90)),
                ('address', models.TextField()),
                ('remarks', models.TextField()),
                ('skills', models.TextField()),
                ('gender', models.CharField(max_length=10)),
                ('experience', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='career_and_intern/apply_job/resumes')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('intrested_in', models.CharField(max_length=70)),
                ('education', models.CharField(max_length=100)),
                ('collage', models.CharField(max_length=250)),
            ],
        ),
    ]
