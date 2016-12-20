# coding=utf-8
from base_model import BaseModel
from peewee import *


class Product(BaseModel):
    name = CharField(max_length=256)
    description = CharField(max_length=256, null=True)
    images = CharField(default='')
    intro = TextField(null=True)
    props = CharField(default='')
    code = '006'

    class Meta:
        db_table = 'products'
