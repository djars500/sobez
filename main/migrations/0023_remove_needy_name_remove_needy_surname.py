# Generated by Django 4.0.3 on 2022-03-29 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_needy_canjob_alter_needy_hasjob_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='needy',
            name='name',
        ),
        migrations.RemoveField(
            model_name='needy',
            name='surName',
        ),
    ]