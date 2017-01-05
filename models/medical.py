# coding=utf-8
from base_model import BaseModel
from peewee import *


class Medical(BaseModel):
    barcode = CharField(max_length=14, primary_key=True)
    name = CharField()
    english_name = CharField(default=None, null=True)
    image = CharField(default='')
    company = CharField(default=None, null=True)
    address = CharField(default=None, null=True)
    functions = CharField(default=None, null=True)
    functions_desc = CharField(default=None, null=True)
    constituent = CharField(default=None, null=True)
    amount_desc = CharField(default=None, null=True)
    tips = CharField(default=None, null=True)
    props = CharField(default='')
    extra = CharField(default=None, null=True)
    code = '014'

    class Meta:
        db_table = 'medicals'
