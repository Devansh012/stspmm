# Generated by Django 5.0.7 on 2024-11-16 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCI', '0008_dciitem_dci'),
    ]

    operations = [
        migrations.AddField(
            model_name='dciitem',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='dciitem',
            name='dateOfCompletion',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
