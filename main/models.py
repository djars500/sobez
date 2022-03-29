from distutils.command.upload import upload
from re import T
from statistics import mode
from venv import create
from django.db import models
from datetime import datetime
from django.utils import timezone
from authentication.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class StatusHome(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Үйінің жағдайы'
        verbose_name_plural = 'Үйінің жағдайы'
        
        
class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ауылды округ'
        verbose_name_plural = 'Ауылды округтар'


class StatusType(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Статус жағдайы'
        verbose_name_plural = 'Статус жағдайлары'


class Event(models.Model):
    
    type_event = (
        ('Аударылды','Аударылды'),
        ('Берілді', 'Берілді'),
        ('Жеке аударылды', 'Жеке аударылды'),
        
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_event')
    cash = models.IntegerField('Салынған ақша', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField('Тип', choices=type_event, null=True, blank=True, max_length=255)
    needy = models.ForeignKey('Needy', on_delete=models.CASCADE, null=True, blank=True, related_name='needy_event')
    comment = models.TextField('Комментарий', null=True, blank=True)
    def __str__(self):
        return f'{self.user.username}: {self.created_at.date()} '
        
    class Meta:
        verbose_name = 'Оқиға'
        verbose_name_plural = 'Оқигалар'
    

    
class Needy(models.Model):
    
    
    job = (
        ('Жұмысы бар','Жұмысы бар'),
        ('Жұмысы жоқ','Жұмысы жоқ'),
    )
    job_type = (
        ('Жұмысқа жарамды','Жұмысқа жарамды'),
        ('Жұмысы жарамсыз','Жұмысы жарамсыз'),
    )
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='needy_user')
    phone = models.CharField('Телефон нөмірі', max_length=11)
    address = models.CharField('Мекенжайы', max_length=255,)
    region = models.ForeignKey(Region,verbose_name='Аулды округ', on_delete=models.CASCADE,blank=True,null=True)
    iin = models.CharField('ЖСН', max_length=12)
    status = models.ForeignKey(StatusType, verbose_name="Статус жағдайы", on_delete=models.CASCADE, related_name='needies')
    period = models.DateField('Көмек алудың соңғы мерзімі', auto_created=False, null=True,blank=True)
    category = models.ForeignKey(Category, verbose_name="Категориясы",on_delete=models.CASCADE, null=True, blank=True)
    hasJob = models.CharField('Жұмыс тұрағы',max_length=255, choices=job, null=True, blank=True)
    canJob = models.CharField('Жұмыс тұрағы',max_length=255, choices=job_type, blank=True, null=True)
    image = models.ImageField('Сүреті', upload_to='needy/', blank=True, null=True)
    statusHome = models.ForeignKey(StatusHome, verbose_name="Үйінің жағдайы", on_delete=models.CASCADE, blank=True, null=True)
    childTotal = models.IntegerField('Балалар саны', null=True, blank=True)
    getHelp = models.TextField('Қандай көмек алды',null=True,blank=True)
    typeHelp = models.TextField('Қандай көмек қажет',null=True,blank=True)
    comment = models.TextField('Пікір', null=True, blank=True)
    created_at = models.DateTimeField("Жасалған кұні",default=timezone.now)
    updated_at = models.DateTimeField("Дата изменения",auto_now=True)
    owner = models.ForeignKey(User, verbose_name="Заявканы ашқан адам", null=True, blank=True,on_delete=models.CASCADE,related_name="owner")
    changed_onwer = models.ForeignKey(User,null=True, verbose_name="Заявканы өзгерткен адам", blank=True,on_delete=models.CASCADE,related_name="changed_owner")


    def __str__(self):
        return f'{self.user.name} {self.user.surName}'
        
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявкалар'
    

    