# Generated by Django 3.2.4 on 2021-06-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_clase4', '0006_ctacte'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]