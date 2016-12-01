# coding=utf-8
from base_model import BaseModel
from peewee import *
from backend_common.exceptions import BaseError
import backend_common.constants.http_code as http_code


class User(BaseModel):
    username = CharField(max_length=40, unique=True)
    password = CharField(max_length=256, null=True)
    sex = IntegerField(default=0)
    phone_number = CharField(max_length=12, unique=True)
    nick = CharField(max_length=12, null=True)
    avatar = CharField(max_length=512, null=True)
    register_type = IntegerField(default=0)

    code = '002'

    @classmethod
    def PasswordError(cls):
        return BaseError(int(str(http_code.UNAUTHORIZED) + cls.code), u'密码错误')

    @classmethod
    def HasExistError(cls):
        return BaseError(int(str(http_code.FORBIDDEN) + cls.code), u'用户已经存在')

    @classmethod
    def VerifycodeExpiredError(cls):
        return BaseError(int(str(http_code.FORBIDDEN) + cls.code), u'验证码不存在或者已经过期')

    @classmethod
    def VerifycodeError(cls):
        return BaseError(int(str(http_code.FORBIDDEN) + cls.code), u'验证码错误')

    @classmethod
    def NotAuthError(cls):
        return BaseError(int(str(http_code.UNAUTHORIZED) + cls.code), u'你还未登录')

    @classmethod
    def TokenError(cls, errmsg=u'token已经失效'):
        return BaseError(int(str(http_code.UNAUTHORIZED) + cls.code), errmsg)

    def tokens(self):
        import backend_common.constants.user_type as user_type
        from user_token import UserToken as UserTokenModel
        user_tokens = []
        q = UserTokenModel.select().where(UserTokenModel.user_type == user_type.USER, UserTokenModel.user_id == self.id)
        for x in q:
            user_tokens.append(x.token)
        return user_tokens

    class Meta:
        db_table = 'users'
