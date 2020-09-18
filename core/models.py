from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('A', 'Atıştırmalık'),
    ('I', 'İçecek'),
    ('D', 'Dondurulmuş'),
    ('K', 'Kuru')
)

ID_CHOICES = (
    ('ID', 'TC Kimlik Numarası'),
    ('NO', 'Vergi Numarası')
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    # one_click_purchasing = models.BooleanField(default=False)
    # id_choice = models.CharField(
    #     max_length=2,
    #     choices=ID_CHOICES,
    #     default='ID'
    # )

    # location = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    # def get_add_to_cart_url(self):
    #     return reverse("core:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })

    # def get_remove_from_cart_url(self):
    #     return reverse("core:remove-from-cart", kwargs={
    #         'slug': self.slug
    #     })


# class Refund(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     reason = models.TextField()
#     accepted = models.BooleanField(default=False)
#     email = models.EmailField()
#
#     def __str__(self):
#         return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
