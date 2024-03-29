# Generated by Django 5.0.1 on 2024-01-16 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_modules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=254)),
                ('module', models.CharField(max_length=50)),
                ('header_ids', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Intrested in Free Demo',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('icon', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('path', models.CharField(max_length=250)),
                ('priority', models.IntegerField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='records.header')),
            ],
            options={
                'verbose_name_plural': 'Headers',
            },
        ),
    ]
