# Generated by Django 5.0.7 on 2024-08-08 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_remove_groupposts_post_group_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='post',
        ),
        migrations.AddField(
            model_name='groupposts',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='groups.group'),
        ),
    ]
