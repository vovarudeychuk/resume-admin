# Generated by Django 4.2.7 on 2023-12-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='project',
            name='image_src',
            field=models.ImageField(default='', upload_to='project-images/'),
        ),
    ]
