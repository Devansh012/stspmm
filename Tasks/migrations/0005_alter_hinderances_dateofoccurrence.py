# Generated by Django 5.0.7 on 2024-09-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0004_alter_tasks_assignmentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hinderances',
            name='dateOfOccurrence',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Occurance'),
        ),
    ]
