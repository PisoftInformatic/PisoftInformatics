# Generated by Django 4.2.7 on 2023-11-24 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_alter_childheader_options_alter_childheader_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='childheader',
            options={'ordering': ['priority']},
        ),
        migrations.AlterModelOptions(
            name='header',
            options={},
        ),
        migrations.AlterField(
            model_name='childheader',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.header'),
        ),
        migrations.AlterModelTable(
            name='childheader',
            table=None,
        ),
        migrations.AlterModelTable(
            name='header',
            table=None,
        ),
    ]
