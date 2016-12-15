# coding=utf-8
from base_model import BaseModel
from peewee import *


class ProductInstance(BaseModel):
    sku_id = IntegerField()
    product_code = CharField()
    order_id = IntegerField()
    code = '010'

    class Meta:
        db_table = 'product_instances'
