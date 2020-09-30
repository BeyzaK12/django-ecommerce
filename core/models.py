from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.dispatch import receiver


class Ürün(models.Model):
    isim = models.CharField(default='', blank=False, max_length=100)
    fiyat = models.FloatField(default=0)
    indirimli_fiyat = models.FloatField(blank=True, null=True)
    fotoğraf = models.ImageField(null=True)

    def __str__(self):
        return self.isim


class Öne_Çıkanlar_Ürün(models.Model):
    isim = models.CharField(default='', blank=False, max_length=100)
    fotoğraf = models.ImageField(null=True)
    açıklama = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.isim

# class Refund(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     reason = models.TextField()
#     accepted = models.BooleanField(default=False)
#     email = models.EmailField()
#
#     def __str__(self):
#         return f"{self.pk}"
