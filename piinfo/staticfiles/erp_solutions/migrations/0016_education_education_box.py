# Generated by Django 4.2.6 on 2023-10-31 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_solutions', '0015_automobile_automobile_box_remove_postimage_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_heading', models.CharField(max_length=50)),
                ('page_description', models.TextField()),
                ('heading_for_box_section', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Education_Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_image', models.FileField(help_text='Make sure your all image have same dimensions and have no background for better Appearence.', upload_to='erp_solutions/images')),
                ('box_heading', models.CharField(help_text='Maximum Length 70 Chars.', max_length=70)),
                ('box_description', models.CharField(max_length=250)),
                ('card', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='erp_solutions.education')),
            ],
        ),
    ]
