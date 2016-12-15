# coding=utf-8
from base_model import BaseModel
from peewee import *


class Sku(BaseModel):
    product_id = IntegerField()
    sku_code = IntegerField()
    market_price = DecimalField(decimal_places=2)
    sales_price = DecimalField(decimal_places=2)
    image = CharField()
    props = CharField()
    stock_count = IntegerField()
    sales_count = IntegerField()
    comment_count = IntegerField()
    code = '007'

    class Meta:
        db_table = 'skus'
