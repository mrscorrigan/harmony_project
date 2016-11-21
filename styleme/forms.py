from django import forms
# from .models import Styleme, Clothing_Item
from django.db import models
from django.contrib.auth.models import User

# class UserPostForm(forms.ModelForm):
#     class Meta:
#         user = models.ForeignKey(User, unique=True)
#         model = Styleme
#         fields = ('name', 'description', 'image')
#         image = forms.ImageField()
#
# class UserPostOutfitForm(forms.ModelForm):
#     class Meta_data:
#         user = models.ForeignKey(User, unique=True)
#         model = clothing_Item
#         fields = ('image', 'name', 'owner')
#         image = forms.ImageField()