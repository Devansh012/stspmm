# Generated by Django 5.0.7 on 2024-09-27 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCI', '0007_remove_dci_project'),
        ('Project', '0010_alter_project_sector_alter_projectlead_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='finalDCI',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DCI.dci'),
        ),
    ]
