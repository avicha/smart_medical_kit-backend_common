# coding=utf-8
from base_model import BaseModel
from peewee import *


class MedicalKit(BaseModel):
    product_code = IntegerField(primary_key=True)
    name = CharField()
    image = CharField()
    box_count = IntegerField()
    code = '010'

    class Meta:
        db_table = 'medical_kits'
