# Generated by Django 4.0.3 on 2022-04-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_needy_lat_alter_needy_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needy',
            name='lat',
            field=models.FloatField(default=43.0401635),
        ),
        migrations.AlterField(
            model_name='needy',
            name='lon',
            field=models.FloatField(default=69.3886292),
        ),
    ]
