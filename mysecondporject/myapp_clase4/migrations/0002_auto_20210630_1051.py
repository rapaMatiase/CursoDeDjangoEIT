# Generated by Django 3.2.4 on 2021-06-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_clase4', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='date_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]