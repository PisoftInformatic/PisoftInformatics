# Generated by Django 4.2.7 on 2023-11-25 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0017_alter_header_options_alter_header_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='header',
            options={'verbose_name_plural': 'Header'},
        ),
        migrations.RemoveField(
            model_name='header',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='header',
            name='path',
        ),
        migrations.AlterField(
            model_name='header',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='header',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='records.header')),
            ],
        ),
    ]
