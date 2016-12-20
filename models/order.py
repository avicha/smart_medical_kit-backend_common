# coding=utf-8
from base_model import BaseModel
from peewee import *
from datetime import datetime


class Order(BaseModel):
    user_id = IntegerField()
    logistics_user_address_id = IntegerField()
    status = IntegerField()
    remark = CharField()
    total_price = DecimalField(decimal_places=2)
    paid_price = DecimalField(decimal_places=2)
    paid_time = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S', null=True)
    code = '008'

    class Meta:
        db_table = 'orders'
