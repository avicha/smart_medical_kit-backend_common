# coding=utf-8
from base_model import BaseModel
from peewee import *


class Address(BaseModel):
    province_code = IntegerField()
    province = CharField(max_length=40)
    city_code = IntegerField()
    city = CharField(max_length=40)
    region_code = IntegerField()
    region = CharField(max_length=40)
    code = '004'

    class Meta:
        db_table = 'addresses'
