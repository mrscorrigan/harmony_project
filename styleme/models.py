from __future__ import unicode_literals
from django.shortcuts import render
from django.db import models
from django.conf import settings
from accounts import models as accounts_models

# Create your models here.


class ClothingItem(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    name = models.CharField(max_length=254, default='')
    # tag = models.CharField(max_length=30, blank=True, null=True)
    owner = models.ForeignKey('accounts.User', related_name='itemsOfClothing')
    def __str__(self):
        return self.name

class Outfit(models.Model):
    owner = models.ForeignKey('accounts.User', related_name='outfits')
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=254, default='')
    items = models.ManyToManyField(ClothingItem)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name



#
# class Item(models.Model):
#     name = models.CharField(max_length=254, default='')
#     description = models.TextField()
#     image = models.ImageField(upload_to='images', default='images/new-product.jpg')
#


    # @property
    # def paypal_form(self):
    #     paypal_dict = {
    #         "business": settings.PAYPAL_RECEIVER_EMAIL,
    #         "amount": self.price,
    #         "currency": "USD",
    #         "item_name": self.name,
    #         "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
    #         "notify_url": settings.PAYPAL_NOTIFY_URL,
    #         "return_url": "%s/paypal-return" % settings.SITE_URL,
    #         "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
    #     }
    #
    #     return PayPalPaymentsForm(initial=paypal_dict)


    def __unicode__(self):
        return self.name






