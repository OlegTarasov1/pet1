# Generated by Django 5.0.7 on 2024-08-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_alter_groupposts_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupposts',
            name='file',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='post/'),
        ),
    ]
