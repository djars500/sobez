# Generated by Django 4.0.3 on 2022-03-23 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatusHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Вид помощи дома',
                'verbose_name_plural': 'Виды помощи домам',
            },
        ),
        migrations.CreateModel(
            name='Needy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surName', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('iin', models.CharField(max_length=12, verbose_name='ИИН')),
                ('childTotal', models.IntegerField(blank=True, null=True, verbose_name='Количество детей')),
                ('getHelp', models.TextField(blank=True, null=True, verbose_name='Какую помощь получили')),
                ('period', models.CharField(blank=True, max_length=255, null=True, verbose_name='Срок получение')),
                ('typeHelp', models.TextField(blank=True, null=True, verbose_name='Какая помощь необходима')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Получили помощь'), (1, 'В разработке'), (2, 'Не полученные')], null=True, verbose_name='Стадия помощи')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('changed_onwer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='changed_owner', to=settings.AUTH_USER_MODEL, verbose_name='Изменитель заявки')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Создатель заявки')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.region', verbose_name='Регион')),
                ('statusHome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.statushome', verbose_name='Статус дома')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
