# Generated by Django 5.0.7 on 2024-11-16 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCI', '0009_dciitem_completed_dciitem_dateofcompletion'),
        ('Tasks', '0013_alter_tasks_dciitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='actualDateOfCompletion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='dciItem',
            field=models.ManyToManyField(to='DCI.dciitem'),
        ),
    ]
