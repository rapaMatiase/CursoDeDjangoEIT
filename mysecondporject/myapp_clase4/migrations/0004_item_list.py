# Generated by Django 3.2.4 on 2021-06-30 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_clase4', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp_clase4.list'),
        ),
    ]