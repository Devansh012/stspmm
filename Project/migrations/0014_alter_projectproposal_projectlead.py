# Generated by Django 5.0.7 on 2024-10-07 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0013_alter_projectproposal_doccontrolindex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectproposal',
            name='projectLead',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.projectlead'),
        ),
    ]
