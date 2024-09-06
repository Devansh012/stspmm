# Generated by Django 5.0.7 on 2024-09-04 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_contactperson_address_contactperson_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScopeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='scopeitem',
            name='scopeGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scope_items', to='Project.scopegroup'),
        ),
    ]
