# Generated by Django 3.2.4 on 2021-07-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_clase5_bonus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articuloporcompra',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]
