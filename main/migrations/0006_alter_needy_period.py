# Generated by Django 4.0.3 on 2022-03-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needy',
            name='period',
            field=models.DateField(blank=True, null=True, verbose_name='Срок получение'),
        ),
    ]
