# Generated by Django 4.0.3 on 2022-04-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_name_user_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
