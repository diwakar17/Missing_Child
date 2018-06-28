#-*- coding: utf-8 -*-s
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=700,blank=True)
    # location = models.CharField(max_length=50, blank=True)
    # birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender= User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Child(models.Model):
    user= models.ForeignKey(Profile,default=1)
    name = models.CharField(max_length=400, blank=False)
    age = models.IntegerField(blank=False)
    details = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to = 'pic_folder/',default='pic_folder/no-image.jpg' )
