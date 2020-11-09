# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Product(models.Model):
    product_class_id = models.IntegerField()
    product_id = models.IntegerField(unique=True, primary_key=True )
    brand_name = models.CharField(max_length=60, blank=True, null=True)
    product_name = models.CharField(max_length=60)
    sku = models.BigIntegerField(db_column='SKU')  # Field name made lowercase.
    srp = models.DecimalField(db_column='SRP', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gross_weight = models.FloatField(blank=True, null=True)
    net_weight = models.FloatField(blank=True, null=True)
    recyclable_package = models.BooleanField(blank=True, null=True)
    low_fat = models.BooleanField(blank=True, null=True)
    units_per_case = models.SmallIntegerField(blank=True, null=True)
    cases_per_pallet = models.SmallIntegerField(blank=True, null=True)
    shelf_width = models.FloatField(blank=True, null=True)
    shelf_height = models.FloatField(blank=True, null=True)
    shelf_depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product'
