# Generated by Django 5.0.7 on 2024-08-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_rename_image_groupposts_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupposts',
            name='file',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='post/%Y/%m/%d/'),
        ),
    ]
