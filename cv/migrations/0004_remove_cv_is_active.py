# Generated by Django 4.2.7 on 2023-11-28 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_cv_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='is_active',
        ),
    ]