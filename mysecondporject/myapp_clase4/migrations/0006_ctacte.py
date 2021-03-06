# Generated by Django 3.2.4 on 2021-06-30 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp_clase4', '0005_list_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CtaCte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mount', models.FloatField()),
                ('badge', models.CharField(choices=[('D', 'Dolares'), ('P', 'Pesos')], default='Dolares', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
