# Generated by Django 2.2.24 on 2021-11-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymeetups', '0004_auto_20211104_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, to='mymeetups.Participant'),
        ),
    ]
