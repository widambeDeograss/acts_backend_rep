# Generated by Django 3.2.20 on 2023-08-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.DeleteModel(
            name='EventFile',
        ),
    ]
