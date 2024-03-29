# Generated by Django 4.2.6 on 2023-10-18 09:11

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_services', '0005_alter_domain_registration_card_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain_registration_card',
            name='description',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='domain_registration_card',
            name='heading',
            field=models.CharField(blank=True, default='', help_text='<150 Chars', max_length=150),
        ),
        migrations.AlterField(
            model_name='domain_registration_card',
            name='sub_heading',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
