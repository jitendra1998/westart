# Generated by Django 2.0.3 on 2018-03-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180325_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='type',
            field=models.IntegerField(null=True),
        ),
    ]