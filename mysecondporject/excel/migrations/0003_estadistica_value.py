# Generated by Django 3.2.4 on 2021-07-08 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0002_alter_myfiles_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.FloatField()),
                ('estadistica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excel.estadistica')),
            ],
        ),
    ]