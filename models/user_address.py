# coding=utf-8
from base_model import BaseModel
from peewee import *


class UserAddress(BaseModel):
    user_id = IntegerField()
    region_code = IntegerField()
    street = CharField(max_length=512)
    is_default = BooleanField(constraints=[SQL('DEFAULT 0')])
    consignee = CharField(max_length=20)
    contact = CharField(max_length=20)
    code = '005'

    class Meta:
        db_table = 'user_addresses'
