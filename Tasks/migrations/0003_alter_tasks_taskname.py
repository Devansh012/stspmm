# Generated by Django 5.0.7 on 2024-09-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_alter_hinderancefollowup_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='taskName',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Task Name'),
        ),
    ]
