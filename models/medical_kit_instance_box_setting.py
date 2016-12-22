# coding=utf-8
from base_model import BaseModel
from peewee import *


class MedicalKitInstanceBoxSetting(BaseModel):
    medical_kit_instance_id = IntegerField()
    box_index = IntegerField()
    medical_name = CharField()
    medical_barcode = IntegerField(null=True)
    schedule = CharField()
    code = '013'

    class Meta:
        db_table = 'medical_kit_instance_box_settings'
