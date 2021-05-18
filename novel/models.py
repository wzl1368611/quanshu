# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Charpter(models.Model):
    charpterid = models.AutoField(primary_key=True)
    novelid = models.ForeignKey('Novel', models.DO_NOTHING, db_column='novelid', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    sid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charpter'


class Novel(models.Model):
    novelid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    sort = models.CharField(max_length=100, blank=True, null=True)
    novelname = models.CharField(max_length=100, blank=True, null=True)
    novelimg = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    author = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'novel'
