# Generated by Django 5.0.3 on 2024-05-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapi', '0018_remove_approvedinflowtransaction_return_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menuIcon',
            field=models.CharField(default='xy', max_length=500),
        ),
    ]