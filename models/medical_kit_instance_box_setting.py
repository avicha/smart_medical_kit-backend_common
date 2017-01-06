# coding=utf-8
from base_model import BaseModel
from peewee import *


class MedicalKitInstanceBoxSetting(BaseModel):
    medical_kit_instance_id = IntegerField()
    box_index = IntegerField()
    medical_name = CharField(default='')
    medical_barcode = IntegerField(default=None, null=True)
    schedule_times = CharField(default='')
    piece_per_time = IntegerField(default=1)
    unit = CharField(default='粒')
    code = '013'

    class Meta:
        db_table = 'medical_kit_instance_box_settings'
