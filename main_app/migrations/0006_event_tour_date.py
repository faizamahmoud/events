# Generated by Django 4.1.1 on 2022-10-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_event_livestream'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tour_date',
            field=models.CharField(default='TBD', max_length=150),
        ),
    ]