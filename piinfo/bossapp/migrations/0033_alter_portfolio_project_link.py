# Generated by Django 5.0.1 on 2024-01-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bossapp', '0032_alter_portfolio_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_link',
            field=models.CharField(blank=True, default='#no_link', help_text='Enter domain name of Your Project. ex - www.xyz.com', max_length=250, null=True),
        ),
    ]
