# coding=utf-8
from base_model import BaseModel
from peewee import *


class ProductInstance(BaseModel):
    product_code = CharField(max_length=15, primary_key=True)
    sku_id = IntegerField()
    order_id = IntegerField(null=True)
    code = '010'

    class Meta:
        db_table = 'product_instances'
