from django.db import models
from django.urls import reverse
from django.utils import timezone
from authentication.models import User
from home.models import RuralDistrict, Localities
from status.models import StatusHome, StatusType, Category
from django_admin_geomap import GeoItem

# from payments import PurchasedItem
# from payments.models import BasePayment

# class Payment(BasePayment):

#     def get_failure_url(self) :
#         # Return a URL where users are redirected after
#         # they fail to complete a payment:
#         return 'http://example.com/failure/'

#     def get_success_url(self) :
#         # Return a URL where users are redirected after
#         # they successfully complete a payment:
#         return 'http://example.com/success/'

#     def get_purchased_items(self):
#         yield PurchasedItem(
#             name='The Hound of the Baskervilles',
#             sku='BSKV',
#             quantity=9,
#             price=Decimal(10),
#             currency='USD',
#         )

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
    needy_family = models.ForeignKey('Family', on_delete=models.CASCADE, null=True, blank=True, related_name='needy_family_event')
    comment = models.TextField('Комментарий', null=True, blank=True)
    file = models.FileField('Бұйрық', upload_to='files/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username}: {self.created_at.date()} '
        
    class Meta:
        verbose_name = 'Оқиға'
        verbose_name_plural = 'Оқигалар'
    
class Family(models.Model,GeoItem):
    
    main_family = models.ForeignKey('Needy', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Отбасының үлкені', related_name='main')
    address = models.CharField('Мекен жайы', max_length=255)
    region = models.ForeignKey(RuralDistrict,verbose_name='Аулды округ', on_delete=models.CASCADE,blank=True,null=True)
    eldimeken = models.ForeignKey(Localities, verbose_name='Елдімекен', on_delete=models.CASCADE,blank=True,null=True)
    lat = models.FloatField(
                 null=True, blank=True )

    lon = models.FloatField(
                 null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Отбасы'
        verbose_name_plural = 'Отбасылар'
    
    def __str__(self):
        return self.address
    
    
    
    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)
    
    def geomap_popup_view(self):
        return f"<a>{self.main_family}</a><br><strong>{self.address}</strong><br>"

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view
    
class Needy(models.Model, GeoItem,):
    
    
    job = (
        ('Жұмысы бар','Жұмысы бар'),
        ('Жұмысы жоқ','Жұмысы жоқ'),
    )
    job_type = (
        ('Жұмысқа жарамды','Жұмысқа жарамды'),
        ('Жұмысы жарамсыз','Жұмысы жарамсыз'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='needy_user',)
    phone = models.CharField('Телефон нөмірі', max_length=11)
    address = models.CharField('Мекенжайы', max_length=255,)
    iin = models.CharField('ЖСН', max_length=12)
    family = models.ForeignKey('Family', on_delete=models.CASCADE, blank=True, null=True, related_name='needy_family', verbose_name='Отбасы')
    status = models.ForeignKey(StatusType, verbose_name="Статус жағдайы", on_delete=models.CASCADE, related_name='needies')
    category = models.ForeignKey(Category, verbose_name="Категориясы",on_delete=models.CASCADE, null=True, blank=True)
    hasJob = models.CharField('Жұмыс тұрағы',max_length=255, choices=job, null=True, blank=True)
    canJob = models.CharField('Жұмыс тұрағы',max_length=255, choices=job_type, blank=True, null=True)
    image = models.ImageField('Сүреті', upload_to='needy/', blank=True, null=True)
    statusHome = models.ForeignKey(StatusHome, verbose_name="Үйінің жағдайы", on_delete=models.CASCADE, blank=True, null=True)
    period = models.DateField('Көмек алудың соңғы мерзімі', auto_created=False, null=True,blank=True)
    childTotal = models.IntegerField('Балалар саны', null=True, blank=True)
    getHelp = models.TextField('Қандай көмек алды',null=True,blank=True)
    typeHelp = models.TextField('Қандай көмек қажет',null=True,blank=True)
    comment = models.TextField('Пікір', null=True, blank=True)
    created_at = models.DateTimeField("Жасалған кұні",default=timezone.now)
    updated_at = models.DateTimeField("Дата изменения",auto_now=True)
    owner = models.ForeignKey(User, verbose_name="Заявканы ашқан адам", null=True, blank=True,on_delete=models.CASCADE,related_name="owner")
    changed_onwer = models.ForeignKey(User,null=True, verbose_name="Заявканы өзгерткен адам", blank=True,on_delete=models.CASCADE,related_name="changed_owner")
    lat = models.FloatField(
                default=43.0401635 )

    lon = models.FloatField(
                default=69.3886292)

    def __str__(self):
        return f'{self.user.name} {self.user.surName}'
        
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявкалар'
    
    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)
    
    def geomap_popup_view(self):
        return f"<strong>{self.user}</strong><br><strong>{self.address}</strong><br>"

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view
    
    def get_absolute_url(self):
        return reverse('main/')
    
    

