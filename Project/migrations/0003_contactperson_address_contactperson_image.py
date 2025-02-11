# Generated by Django 5.0.7 on 2024-08-31 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_alter_staff_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactperson',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contact_images/'),
        ),
    ]
