# Generated by Django 4.2.7 on 2023-11-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_about_about_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_text',
            field=models.JSONField(default=''),
        ),
    ]