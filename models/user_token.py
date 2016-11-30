# coding=utf-8
from base_model import BaseModel
from peewee import *


class UserToken(BaseModel):
    user_id = IntegerField()
    user_type = IntegerField()
    token = CharField(max_length=512)
    code = '003'

    class Meta:
        db_table = 'user_tokens'
