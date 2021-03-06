# Generated by Django 4.0.3 on 2022-04-27 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Мекен жайы')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Лат')),
                ('lng', models.FloatField(blank=True, null=True, verbose_name='Лат')),
                ('eldimeken', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.localities', verbose_name='Елдімекен')),
            ],
            options={
                'verbose_name': 'Отбасы',
                'verbose_name_plural': 'Отбасылар',
            },
        ),
        migrations.CreateModel(
            name='Needy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон нөмірі')),
                ('address', models.CharField(max_length=255, verbose_name='Мекенжайы')),
                ('iin', models.CharField(max_length=12, verbose_name='ЖСН')),
                ('hasJob', models.CharField(blank=True, choices=[('Жұмысы бар', 'Жұмысы бар'), ('Жұмысы жоқ', 'Жұмысы жоқ')], max_length=255, null=True, verbose_name='Жұмыс тұрағы')),
                ('canJob', models.CharField(blank=True, choices=[('Жұмысқа жарамды', 'Жұмысқа жарамды'), ('Жұмысы жарамсыз', 'Жұмысы жарамсыз')], max_length=255, null=True, verbose_name='Жұмыс тұрағы')),
                ('image', models.ImageField(blank=True, null=True, upload_to='needy/', verbose_name='Сүреті')),
                ('period', models.DateField(blank=True, null=True, verbose_name='Көмек алудың соңғы мерзімі')),
                ('childTotal', models.IntegerField(blank=True, null=True, verbose_name='Балалар саны')),
                ('getHelp', models.TextField(blank=True, null=True, verbose_name='Қандай көмек алды')),
                ('typeHelp', models.TextField(blank=True, null=True, verbose_name='Қандай көмек қажет')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Пікір')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Жасалған кұні')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='status.category', verbose_name='Категориясы')),
                ('changed_onwer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='changed_owner', to=settings.AUTH_USER_MODEL, verbose_name='Заявканы өзгерткен адам')),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='needy_family', to='main.family', verbose_name='Отбасы')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Заявканы ашқан адам')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needies', to='status.statustype', verbose_name='Статус жағдайы')),
                ('statusHome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='status.statushome', verbose_name='Үйінің жағдайы')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='needy_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявкалар',
            },
        ),
        migrations.AddField(
            model_name='family',
            name='main_family',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='main.needy', verbose_name='Отбасының үлкені'),
        ),
        migrations.AddField(
            model_name='family',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.ruraldistrict', verbose_name='Аулды округ'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.IntegerField(blank=True, null=True, verbose_name='Салынған ақша')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(blank=True, choices=[('Аударылды', 'Аударылды'), ('Берілді', 'Берілді'), ('Жеке аударылды', 'Жеке аударылды')], max_length=255, null=True, verbose_name='Тип')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Бұйрық')),
                ('needy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='needy_event', to='main.needy')),
                ('needy_family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='needy_family_event', to='main.family')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_event', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оқиға',
                'verbose_name_plural': 'Оқигалар',
            },
        ),
    ]
