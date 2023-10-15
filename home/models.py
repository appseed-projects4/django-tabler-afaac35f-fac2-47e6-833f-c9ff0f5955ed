# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Household(models.Model):

    #__Household_FIELDS__
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    owner = models.CharField(max_length=255, null=True, blank=True)

    #__Household_FIELDS__END

    class Meta:
        verbose_name        = _("Household")
        verbose_name_plural = _("Household")


class Transactions(models.Model):

    #__Transactions_FIELDS__
    transaction type = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)

    #__Transactions_FIELDS__END

    class Meta:
        verbose_name        = _("Transactions")
        verbose_name_plural = _("Transactions")


class Residents(models.Model):

    #__Residents_FIELDS__
    first name = models.CharField(max_length=255, null=True, blank=True)
    last name = models.CharField(max_length=255, null=True, blank=True)
    middle name = models.CharField(max_length=255, null=True, blank=True)
    alias = models.CharField(max_length=255, null=True, blank=True)
    place of birth = models.CharField(max_length=255, null=True, blank=True)
    civil status = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    householdno = models.CharField(max_length=255, null=True, blank=True)
    relationship to the owner = models.CharField(max_length=255, null=True, blank=True)

    #__Residents_FIELDS__END

    class Meta:
        verbose_name        = _("Residents")
        verbose_name_plural = _("Residents")


class Blotters(models.Model):

    #__Blotters_FIELDS__
    complainant = models.CharField(max_length=255, null=True, blank=True)
    responder = models.CharField(max_length=255, null=True, blank=True)
    type of incident = models.CharField(max_length=255, null=True, blank=True)
    narrative = models.CharField(max_length=255, null=True, blank=True)
    witness = models.CharField(max_length=255, null=True, blank=True)

    #__Blotters_FIELDS__END

    class Meta:
        verbose_name        = _("Blotters")
        verbose_name_plural = _("Blotters")


class Inventory Items(models.Model):

    #__Inventory Items_FIELDS__
    purchase date = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    date created = models.CharField(max_length=255, null=True, blank=True)

    #__Inventory Items_FIELDS__END

    class Meta:
        verbose_name        = _("Inventory Items")
        verbose_name_plural = _("Inventory Items")


class Health(models.Model):

    #__Health_FIELDS__
    datecreated = models.CharField(max_length=255, null=True, blank=True)
    complain = models.CharField(max_length=255, null=True, blank=True)
    diagnosis = models.CharField(max_length=255, null=True, blank=True)
    prescription = models.CharField(max_length=255, null=True, blank=True)
    type of health service = models.CharField(max_length=255, null=True, blank=True)

    #__Health_FIELDS__END

    class Meta:
        verbose_name        = _("Health")
        verbose_name_plural = _("Health")


class Businesses(models.Model):

    #__Businesses_FIELDS__
    business name = models.CharField(max_length=255, null=True, blank=True)
    business address = models.CharField(max_length=255, null=True, blank=True)
    business owner = models.CharField(max_length=255, null=True, blank=True)
    nature of business = models.CharField(max_length=255, null=True, blank=True)

    #__Businesses_FIELDS__END

    class Meta:
        verbose_name        = _("Businesses")
        verbose_name_plural = _("Businesses")


class Vehicle(models.Model):

    #__Vehicle_FIELDS__
    vehicle type = models.CharField(max_length=255, null=True, blank=True)
    owner name = models.CharField(max_length=255, null=True, blank=True)
    brand and model = models.CharField(max_length=255, null=True, blank=True)

    #__Vehicle_FIELDS__END

    class Meta:
        verbose_name        = _("Vehicle")
        verbose_name_plural = _("Vehicle")



#__MODELS__END
