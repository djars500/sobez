from django.db import models


class RuralDistrict(models.Model):
    name = models.CharField('Ауылдық округ атауы', max_length=255)
    lat = models.FloatField('Лат',null=True,blank=True,)
    lng = models.FloatField('Лат',null=True,blank=True,)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Ауылдық округ'
        verbose_name_plural = 'Ауылдық округтар'
        
class Localities(models.Model):

    name = models.CharField('Елді мекен атауы',max_length=255)
    lat = models.FloatField('Лат',null=True,blank=True,default=42.19705782897213)
    lng = models.FloatField('Лат',null=True,blank=True,default=69.95598711561539)
    rural = models.ForeignKey(RuralDistrict, verbose_name='Ауылдық округ', related_name='localities',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Елді мекен'
        verbose_name_plural = 'Елді мекендер'