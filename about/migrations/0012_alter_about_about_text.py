# Generated by Django 4.2.7 on 2023-12-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_rename_testimonial_about_testimonials_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_text',
            field=models.TextField(default=''),
        ),
    ]
