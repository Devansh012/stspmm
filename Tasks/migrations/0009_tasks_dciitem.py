# Generated by Django 5.0.7 on 2024-09-27 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCI', '0007_remove_dci_project'),
        ('Tasks', '0008_taskactivities_completed_tasks_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='dciItem',
            field=models.ManyToManyField(blank=True, null=True, to='DCI.dciitem'),
        ),
    ]
