# Generated by Django 5.0.7 on 2024-08-03 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DCI', '0001_initial'),
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hinderances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfOccurrence', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cleared', models.BooleanField(blank=True, default=False, null=True)),
                ('clearedDate', models.DateField(blank=True, null=True)),
                ('associatedStaff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.staff')),
                ('dciItem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DCI.dciitem')),
            ],
        ),
        migrations.CreateModel(
            name='HinderanceFollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followUpDate', models.DateField(blank=True, null=True)),
                ('followUpDescription', models.TextField(blank=True, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
                ('hinderance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tasks.hinderances')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(blank=True, max_length=30, null=True)),
                ('taskDescription', models.TextField(blank=True, null=True)),
                ('assignmentDate', models.DateField(blank=True, null=True)),
                ('targetDateOfCompletion', models.DateField(blank=True, null=True)),
                ('assignedTo', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.staff')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
            ],
        ),
        migrations.CreateModel(
            name='TaskActivities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfEntry', models.DateField(auto_now_add=True, null=True)),
                ('activityName', models.CharField(blank=True, max_length=30, null=True)),
                ('activityDescription', models.TextField(blank=True, null=True)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tasks.tasks')),
            ],
        ),
    ]
