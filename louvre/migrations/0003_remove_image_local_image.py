# Generated by Django 4.0.3 on 2022-03-28 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('louvre', '0002_image_local_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='local_image',
        ),
    ]
