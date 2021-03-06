# Generated by Django 4.0.3 on 2022-04-27 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RuralDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ауылдық округ атауы')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Лат')),
                ('lng', models.FloatField(blank=True, null=True, verbose_name='Лат')),
            ],
            options={
                'verbose_name': 'Ауылдық округ',
                'verbose_name_plural': 'Ауылдық округтар',
            },
        ),
        migrations.CreateModel(
            name='Localities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Елді мекен атауы')),
                ('lat', models.FloatField(blank=True, default=42.19705782897213, null=True, verbose_name='Лат')),
                ('lng', models.FloatField(blank=True, default=69.95598711561539, null=True, verbose_name='Лат')),
                ('rural', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localities', to='home.ruraldistrict', verbose_name='Ауылдық округ')),
            ],
            options={
                'verbose_name': 'Елді мекен',
                'verbose_name_plural': 'Елді мекендер',
            },
        ),
    ]
