# Generated by Django 4.2.7 on 2023-11-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('type', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('google_map', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('resume_pdf', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('contacts', models.ManyToManyField(to='account.contact')),
                ('socials', models.ManyToManyField(to='account.social')),
            ],
        ),
    ]
