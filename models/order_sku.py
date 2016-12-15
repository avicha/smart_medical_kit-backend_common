# coding=utf-8
from base_model import BaseModel
from peewee import *


class OrderSku(BaseModel):
    order_id = IntegerField()
    sku_id = IntegerField()
    product_name = CharField(max_length=256)
    product_description = CharField(max_length=256)
    product_images = CharField()
    product_intro = TextField()
    sku_market_price = DecimalField(decimal_places=2)
    sku_sales_price = DecimalField(decimal_places=2)
    sku_image = CharField()
    sku_props = CharField()
    amount = IntegerField()
    code = '009'

    class Meta:
        db_table = 'order_skus'
