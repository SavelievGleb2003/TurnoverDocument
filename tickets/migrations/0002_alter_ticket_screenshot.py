# Generated by Django 5.0.4 on 2025-02-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/tickets_screenshots/'),
        ),
    ]
