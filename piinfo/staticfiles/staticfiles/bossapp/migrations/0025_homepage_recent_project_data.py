# Generated by Django 4.2.6 on 2023-10-24 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bossapp', '0024_delete_desktop_applications_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage_Recent_project_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(help_text='Make Sure Project name is less than 50 chars', max_length=50)),
                ('project_link', models.CharField(help_text="Make Sure your link start only with 'www' only and if your link chars>250 shorten url please", max_length=250)),
                ('project_image', models.ImageField(upload_to='portfolio/display/')),
            ],
        ),
    ]
