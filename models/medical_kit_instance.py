# coding=utf-8
from base_model import BaseModel
from peewee import *


class MedicalKitInstance(BaseModel):
    product_code = IntegerField()
    purchase_channel = IntegerField()
    order_id = IntegerField(null=True)
    code = '011'

    class Meta:
        db_table = 'medical_kit_instances'
