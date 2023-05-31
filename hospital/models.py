# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class NormalH(models.Model):
    id = models.IntegerField(null=False)
    주소 = models.TextField(blank=True, null=True)
    병원분류명 = models.TextField(blank=True, null=True)
    응급의료기관코드명 = models.TextField(blank=True, null=True)
    응급실운영여부 = models.TextField(blank=True, null=True)
    입원가능여부 = models.TextField(blank=True, null=True)
    응급실병상 = models.TextField(blank=True, null=True)
    수술실병상 = models.TextField(blank=True, ll=True)
    입원실병상 = models.TextField(blank=True, null=True)
    기관명 = models.TextField(blank=True, primary_key=True)
    대표전화1 = models.TextField(blank=True, null=True)
    응급실전화 = models.TextField(blank=True, null=True)
    월요진료 = models.TextField(blank=True, null=True)
    화요진료 = models.TextField(blank=True, null=True)
    수요진료 = models.TextField(blank=True, null=True)
    목요진료 = models.TextField(blank=True, null=True)
    금요진료 = models.TextField(blank=True, null=True)
    토요진료 = models.TextField(blank=True, null=True)
    일요진료 = models.TextField(blank=True, null=True)
    공휴일진료 = models.TextField(blank=True, null=True)
    기관ID = models.TextField(blank=True, null=True)  # Field name made lowercase.
    병원경도 = models.TextField(blank=True, null=True)
    병원위도 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalH'

class aedLocation(models.Model):
    aed_id = models.IntegerField(null=False)
    설치기관명 = models.TextField(blank=True, null=True)
    설치장소 = models.TextField(blank=True, null=True)
    관리자 = models.TextField(blank=True, null=True)
    관리자연락처 = models.TextField(blank=True, null=True)
    경도 = models.TextField(blank=True, null=True)
    위도 = models.TextField(blank=True, null=True)
    우편번호 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AED'