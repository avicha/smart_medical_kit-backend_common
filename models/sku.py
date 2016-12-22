# coding=utf-8
from base_model import BaseModel
from peewee import *


class Sku(BaseModel):
    product_id = IntegerField()
    market_price = DecimalField(decimal_places=2)
    sales_price = DecimalField(decimal_places=2)
    image = CharField(null=True)
    props = CharField(default='')
    stock_count = IntegerField(default=0)
    sales_count = IntegerField(default=0)
    comment_count = IntegerField(default=0)
    code = '007'

    class Meta:
        db_table = 'skus'
