# Generated by Django 4.2.7 on 2023-11-24 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0016_alter_header_options_alter_header_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='header',
            options={'verbose_name_plural': 'Headers'},
        ),
        migrations.AlterField(
            model_name='header',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='header',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='records.header'),
        ),
        migrations.DeleteModel(
            name='ChildHeader',
        ),
    ]
