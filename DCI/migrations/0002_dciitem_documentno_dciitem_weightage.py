# Generated by Django 5.0.7 on 2024-08-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dciitem',
            name='documentNo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='dciitem',
            name='weightage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
