# Generated by Django 5.1.1 on 2024-10-22 15:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_core', '0002_clientsettings_show_images_unauthenticated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsettings',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='client_logos', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg', 'webp'])]),
        ),
    ]
