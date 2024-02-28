# Generated by Django 4.2.4 on 2023-12-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0007_importantinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('VIDEO', 'VIDEO'), ('IMAGE', 'IMAGE')], max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/gallery/')),
            ],
        ),
    ]
