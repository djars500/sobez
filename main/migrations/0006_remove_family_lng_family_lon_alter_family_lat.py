# Generated by Django 4.0.3 on 2022-04-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_needy_lat_alter_needy_lon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='lng',
        ),
        migrations.AddField(
            model_name='family',
            name='lon',
            field=models.FloatField(default=69.3886292),
        ),
        migrations.AlterField(
            model_name='family',
            name='lat',
            field=models.FloatField(default=43.0401635),
        ),
    ]
