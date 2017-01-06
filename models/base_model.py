# coding=utf-8
from peewee import *
from database import database
from datetime import datetime
from playhouse.shortcuts import model_to_dict
from backend_common.exceptions import BaseError
import backend_common.constants.http_code as http_code


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S')
    updated_at = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S')
    deleted_at = DateTimeField(null=True, constraints=[SQL('DEFAULT NULL')], formats='%Y-%m-%d %H:%M:%S')

    @classmethod
    def LackOfFieldError(cls, errmsg=u'缺乏参数'):
        return BaseError(int(str(http_code.BAD_REQUEST) + cls.code), errmsg)

    @classmethod
    def NotFoundError(cls, errmsg=u'找不到该模型'):
        return BaseError(int(str(http_code.NOT_FOUND) + cls.code), errmsg)

    def format(self, fields='*'):
        model_dict = model_to_dict(self)
        if fields == '*':
            ret = model_dict
        else:
            ret = {}
            if type(fields) == str:
                fields = fields.split(',')
            for k in fields:
                if k in model_dict:
                    v = model_dict[k]
                else:
                    v = None
                ret[k] = v
        for k in ret:
            v = ret[k]
            if isinstance(v, datetime):
                v = v.strftime("%Y-%m-%d %H:%M:%S")
                ret[k] = v
        return ret

    class Meta:
        database = database
