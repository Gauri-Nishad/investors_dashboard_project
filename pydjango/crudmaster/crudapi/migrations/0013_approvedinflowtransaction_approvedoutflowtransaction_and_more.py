# Generated by Django 5.0.3 on 2024-04-05 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapi', '0012_delete_approvedinflowtransaction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedInflowTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor', models.CharField(max_length=500)),
                ('to_company', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('inflowtransaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapi.inflowtransaction')),
            ],
        ),
        migrations.CreateModel(
            name='ApprovedOutflowTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=500)),
                ('to_company', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('outflowtransaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapi.outflowtransaction')),
            ],
        ),
        migrations.CreateModel(
            name='RejectedInflowTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor', models.CharField(max_length=500)),
                ('to_company', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('inflowtransaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapi.inflowtransaction')),
            ],
        ),
        migrations.CreateModel(
            name='RejectedOutflowTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=500)),
                ('to_company', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('outflowtransaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapi.outflowtransaction')),
            ],
        ),
    ]
