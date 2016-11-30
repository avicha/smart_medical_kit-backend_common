# coding=utf-8
from base_model import BaseModel
from peewee import *
from backend_common.exceptions import BaseError
import backend_common.constants.http_code as http_code


class Admin(BaseModel):
    username = CharField(max_length=40, unique=True)
    password = CharField(max_length=256)
    code = '001'

    def tokens(self):
        import backend_common.constants.user_type as user_type
        from user_token import UserToken as UserTokenModel
        user_tokens = []
        q = UserTokenModel.select().where(UserTokenModel.user_type == user_type.ADMIN, UserTokenModel.user_id == self.id)
        for x in q:
            user_tokens.append(x.token)
        return user_tokens

    @classmethod
    def PasswordError(cls):
        return BaseError(int(str(http_code.FORBIDDEN) + cls.code), u'密码错误')

    @classmethod
    def NotAuthError(cls):
        return BaseError(int(str(http_code.FORBIDDEN) + cls.code), u'你还未登录')

    @classmethod
    def TokenError(cls, errmsg=u'token已经失效'):
        return BaseError(int(str(http_code.FORBIDDEN) + cls.code), errmsg)

    class Meta:
        db_table = 'admins'
