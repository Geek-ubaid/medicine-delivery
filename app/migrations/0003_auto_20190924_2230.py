# Generated by Django 2.0.3 on 2019-09-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190924_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='user_id',
            field=models.CharField(max_length=36),
        ),
    ]
