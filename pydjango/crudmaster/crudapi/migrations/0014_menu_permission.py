# Generated by Django 5.0.3 on 2024-04-08 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapi', '0013_approvedinflowtransaction_approvedoutflowtransaction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuItem', models.CharField(max_length=50)),
                ('menuPath', models.CharField(max_length=50)),
                ('parentID', models.IntegerField()),
                ('sortOrder', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ManyToManyField(to='crudapi.menu')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapi.role')),
            ],
        ),
    ]
