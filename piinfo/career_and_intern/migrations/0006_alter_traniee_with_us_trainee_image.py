# Generated by Django 5.0.1 on 2024-01-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_and_intern', '0005_alter_traniee_with_us_trainee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traniee_with_us',
            name='trainee_image',
            field=models.ImageField(blank=True, default='/no-image.jpg', upload_to='career_and_intern/trainee_with_us'),
        ),
    ]
