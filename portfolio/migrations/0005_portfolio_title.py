# Generated by Django 4.2.7 on 2023-12-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
