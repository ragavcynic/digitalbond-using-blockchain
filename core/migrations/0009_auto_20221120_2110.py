# Generated by Django 3.2.16 on 2022-11-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_inverst_transction_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='eth',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='department',
            name='fund',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
