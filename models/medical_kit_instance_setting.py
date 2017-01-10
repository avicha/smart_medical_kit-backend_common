# coding=utf-8
from base_model import BaseModel
from peewee import *


class MedicalKitInstanceSetting(BaseModel):
    medical_kit_instance_id = IntegerField()
    prompt_sound = CharField(default='text 吃药啦')
    code = '012'

    class Meta:
        db_table = 'medical_kit_instance_settings'
